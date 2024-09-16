from django.contrib import admin
from .models import Article, FAQ, Promo, Job, Review, Company 
# Register your models here.
admin.site.register(Article)
admin.site.register(FAQ)
admin.site.register(Promo)
admin.site.register(Job)
admin.site.register(Review)
admin.site.register(Company)