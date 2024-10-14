import os
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from hotelinfo.models import Partner
import requests
from io import BytesIO

class Command(BaseCommand):
    help = 'Generates 5 sample partners'

    def handle(self, *args, **kwargs):
        partners_data = [
            {"name": "TechCorp", "url": "https://techcorp.com", "logo":"logo1.png"},
            {"name": "EcoSolutions", "url": "https://ecosolutions.org", "logo":"logo2.png"},
            {"name": "GlobalTravel", "url": "https://globaltravel.com", "logo":"logo3.png"},
            {"name": "FinanceHub", "url": "https://financehub.net", "logo":"logo4.png"},
            {"name": "HealthPlus", "url": "https://healthplus.org", "logo":"logo5.png"},
        ]
        for data in partners_data:
            logo_path = os.path.join(settings.BASE_DIR, "static/" + data['logo'])
            if os.path.exists(logo_path):
                with open(logo_path, 'rb') as f:
                    partner = Partner(name=data['name'], url=data['url'])
                    partner.logo.save(data['logo'], File(f), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully created partner: {data["name"]}'))
            else:
                self.stdout.write(self.style.ERROR(f'Logo file not found for partner: {data["name"]}'))