import random
from faker import Faker
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import *
from hotelsystem.models import *
from hotelinfo.models import *


def seed_data():
    fake = Faker()
    User = get_user_model()

    # Create superuser
    User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')

    # Create clients
    clients = []
    for i in range(10):
        user = User.objects.create_user(
            username= "+37525797447" + str(i),
            email=fake.email(),
            password="!Qwerty1"
        )
        client = Client.objects.create(
            user=user,
            phone_number=user.username,
            count_of_childs=random.randint(0, 5),
            date_of_birth=fake.date_of_birth(),
        )
        clients.append(client)

    # Create employees
    employees = []
    for i in range(5):
        user = User.objects.create_user(
            username="+37525797446" + str(i),
            email=fake.email(),
            password="!Qwerty1",
            is_staff=True
        )
        employee = Employee.objects.create(
            user=user,
            phone_number=user.username,
            salary=random.uniform(1000, 5000),
            date_of_birth=fake.date_of_birth(),
            # image=fake.image_url(width=None, height=None)
        )
        employees.append(employee)
    

    # Create job titles
    job_titles = []
    for _ in range(3):
        job_title = JobTitle.objects.create(
            title=fake.job(),
            description=fake.catch_phrase()
        )
        job_title.employees.set(random.sample(employees, 2))
        job_titles.append(job_title)

    promos = []
    for _ in range(5):
        promo = Promo.objects.create(
            title=fake.sentence(nb_words=4),
            description=fake.text(max_nb_chars=200),
            start_date=timezone.now(),
            expire_date=fake.future_datetime(end_date='+1d'),
            amount=random.uniform(10, 100),
            status=random.choice(['1', '2'])
        )
        promos.append(promo)

    # Create promo instances
    for client in clients:
        for promo in promos:
            PromoInstance.objects.create(
                status=random.choice(['1', '2']),
                client=client,
                promo=promo,
                amount=random.uniform(10, 100)
            )

    # Create articles
    # for _ in range(5):
    #     Article.objects.create(
    #         title=fake.sentence(nb_words=4),
    #         summary=fake.text(max_nb_chars=200),
    #         body=fake.text(max_nb_chars=1000),
    #         # image=fake.image_url(width=None, height=None),
    #         last_modified_date=timezone.now()
    #     )

    # # Create FAQs
    # for _ in range(5):
    #     FAQ.objects.create(
    #         question=fake.sentence(nb_words=6),
    #         answer=fake.text(max_nb_chars=200)
    #     )

    # # Create jobs
    # for _ in range(5):
    #     Job.objects.create(
    #         title=fake.job(),
    #         description=fake.text(max_nb_chars=500)
    #     )

    # # Create reviews
    # for client in clients:
    #     Review.objects.create(
    #         body=fake.paragraph(nb_sentences=3),
    #         user=client.user
    #     )

    # # Create companies
    # for _ in range(3):
    #     Company.objects.create(
    #         title=fake.company(),
    #         description=fake.text(max_nb_chars=500)
    #     )

    # Create room categories
    room_categories = []
    for _ in range(3):
        category = RoomCategory.objects.create(
            name=fake.word()
        )
        room_categories.append(category)

    # Create rooms
    rooms = []
    for _ in range(10):
        room = Room.objects.create(
            number=fake.random_int(min=100, max=999),
            category=random.choice(room_categories),
            description=fake.text(max_nb_chars=200),
            status='1',
            capacity=random.randint(1, 4),
            one_day_cost=random.uniform(50, 300)
        )
        rooms.append(room)

    # # Create room images
    # for room in rooms:
    #     Image.objects.create(
    #         room=room,
    #         image=fake.image_url(width=None, height=None)
    #     )

    # Create reservations
    # for client in clients:
    #     Reservation.objects.create(
    #         user=client.user,
    #         adults_count=random.randint(1, 4),
    #         start_date=fake.date_time_this_year(),
    #         end_date=fake.date_time_this_year(),
    #         price=random.uniform(50, 200)
    #     )

    # Create payments
    # for client in clients:
    #     reservation = Reservation.objects.filter(user=client.user).first()
    #     Payment.objects.create(
    #         user=client.user,
    #         description=fake.text(max_nb_chars=200),
    #         reservation=reservation,
    #         amount=random.uniform(10, 100)
    #     )


if __name__ == '__main__':
    seed_data()