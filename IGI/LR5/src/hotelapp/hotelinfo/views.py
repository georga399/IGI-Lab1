import logging
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Company, Article

logger = logging.getLogger(__name__)

# Create your views here.
def policy(request):
    return render(request, 'policy.html')

def about(request):
    company = Company.objects.first()  # or get the company instance however you need
    logger.info('Company details: %s', company)
    return render(request, 'about.html', context={'company': company})

def general(request):
    article = Article.objects.first()
    return render(request, 'general.html',{'article': article})

def news(request):
    news = Article.objects.all()
    return render(request, 'news.html', {'news': news})

def article(request, id):
    article = None
    try:
        article = Article.objects.get(id=id)
    except:
        pass

    if article is None:
        return HttpResponseNotFound()
    else:
        return render(request, 'article', {'article': article})