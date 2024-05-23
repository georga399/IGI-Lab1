import logging
import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
import django.contrib.auth as auth
from django.contrib.auth.models import Group, User

from .forms import UserRegisterForm
from .models import Client, Employee


# Create your views here.
logger = logging.getLogger(__name__)

def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get("username")
        print(f"username: {username}")

        if(form.is_valid()):
            if (len(User.objects.filter(username=request.POST.get("username"))) != 0):
                return redirect('/login/')
            age_check = datetime.datetime.strptime(request.POST['agecheck'], "%Y-%m-%d")

            if age_check > datetime.datetime.now() - datetime.timedelta(days=18*365):
                messages.warning(request, "You must be at least 18 years old to register")
                return redirect('login')

            user = form.save()

            group = Group.objects.get(name='client')
            user.groups.add(group)

            client = Client(
                user=user, phone_number=username, count_of_childs=request.POST.get("count_of_childs"),
                date_of_birth=request.POST.get("date_of_birth")
            )
            client.save()
            messages.success(request, "User was created")

            return redirect('/login/')
        else: 
            messages.warning(request, "Invalid form")

    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


    return render(request, 'base.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")
        context = {}
        return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'base.html')