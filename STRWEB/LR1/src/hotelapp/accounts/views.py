import logging
import datetime
from django.utils import timezone
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
        return redirect('general')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get("username")
        print(f"username: {username}")

        if(form.is_valid()):
            if (len(User.objects.filter(username=request.POST.get("username"))) != 0):
                return redirect('/login/')
            age_check = datetime.datetime.strptime(request.POST['date_of_birth'], "%Y-%m-%d")

            if age_check > datetime.datetime.now() - datetime.timedelta(days=18*365):
                messages.warning(request, "You must be at least 18 years old to register")
                return redirect('login')

            user = form.save()

            # group = Group.objects.get(name='client')
            # user.groups.add(group)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()

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
        if request.user.is_staff:
            return redirect('staff_cabinet')
        else:
            return redirect('personal_cabinet')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # tz = timezone.get_current_timezone()
                response = redirect('personal_cabinet')
                
                if request.user.is_staff:
                    response = redirect('staff_cabinet')

                # response.set_cookie("django_timezone", str(tz))
                return response
            else:
                messages.info(request, "Username or Password is incorrect")
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('general')
