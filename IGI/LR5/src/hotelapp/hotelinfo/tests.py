from datetime import timedelta
import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from accounts.models import Employee
from .models import Article, FAQ, Job, Review, Company, Promo
from .views import policy, about, general, news, faq, article, contacts, vacancy, reviews, add_review, promos, joker

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_policy_view(self):
        response = self.client.get(reverse('policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policy.html')

    def test_about_view(self):
        company = Company.objects.create(title='Test Company', description='Test description')
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertEqual(response.context['company'], company)

    def test_general_view(self):
        article = Article.objects.create(title='Test Article', summary='Test summary', body='Test body')
        response = self.client.get(reverse('general'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'general.html')
        self.assertEqual(response.context['article'], article)

    def test_news_view(self):
        Article.objects.create(title='Test Article 1', summary='Test summary 1', body='Test body 1')
        Article.objects.create(title='Test Article 2', summary='Test summary 2', body='Test body 2')
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertEqual(len(response.context['articles']), 2)

    def test_faq_view(self):
        FAQ.objects.create(question='Test question', answer='Test answer')
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')
        self.assertEqual(len(response.context['faq']), 1)

    def test_article_view(self):
        article = Article.objects.create(title='Test Article', summary='Test summary', body='Test body')
        response = self.client.get(reverse('article', args=[article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')
        self.assertEqual(response.context['article'], article)


    def test_vacancy_view(self):
        Job.objects.create(title='Test Job', description='Test description')
        response = self.client.get(reverse('vacancy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        self.assertEqual(len(response.context['jobs']), 1)




