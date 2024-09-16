from pyexpat.errors import messages
import requests
from django.utils import timezone
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from accounts.models import Employee
from .models import Company, Article, FAQ, Job, Promo, Review
from .forms import ReviewForm

logger = logging.getLogger(__name__)

def policy(request):
    logger.info("GET policy page")
    return render(request, 'policy.html')

def about(request):
    company = Company.objects.first()
    logger.info('Company details: %s', company)
    return render(request, 'about.html', context={'company': company})

def general(request):
    article = None
    try:
        article = Article.objects.latest('last_modified_date')
    except:
        return render(request, 'base.html')
    return render(request, 'general.html',{'article': article})

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def news(request):
    news = Article.objects.all()
    logger.info(f"Get article counts: {len(news)}")
    return render(request, 'news.html', {'articles': news})

def faq(request):
    faqs = FAQ.objects.all()
    response = requests.get('https://catfact.ninja/fact')
    fact = response.json()
    data = {'fact': fact}
    
    logger.info(f"Get faqs. Count: {len(faqs)}")
    return render(request, 'faq.html', {'faq': faqs, 'fact': fact})

def article(request, id):
    article = None
    try:
        article = Article.objects.get(id=id)
    except:
        return HttpResponseNotFound('Article not found')
    return render(request, 'article.html', {'article': article})

def contacts(request):
    employees = Employee.objects.all()
    return render(request, 'contacts.html', {'employees': employees})

def vacancy(request):
    jobs = Job.objects.all()
    return render(request, 'vacancy.html', {'jobs': jobs})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def promos(request):
    current_time = timezone.now()
    logger.info(f"GET promos: current_time to get promos {current_time}")

    active_promos = Promo.objects.filter(start_date__lte=current_time, expire_date__gte=current_time)
    archived_promos = Promo.objects.filter(expire_date__lt=current_time)

    return render(request, 'promotions.html', {'active_promos': active_promos, 'archived_promos': archived_promos})

@login_required
def joker(request):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    data = {'joke': joke}
    logger.info(f"Joke: {joke}")
    return render(request, 'joker.html', {'joke': joke})