from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Products,Doctor,Deals,Schedule
from .forms import Add_product,Add_Doctor,ScheduleAppointment,Add_Deals
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def Home(request):
     if request.user.is_authenticated:
        return render(request, 'base.html')
     else:
          messages.error(request, "Please log in first.")
          return redirect('login')
def count(request):
     if request.user.is_authenticated:
        product_count = Products.objects.count()
        doctor_count = Doctor.objects.count()
        today = datetime.now().date()
        schedules = Schedule.objects.filter(Date_Of_Schedule=today).count()
        deals = Deals.objects.all()
        context = {
            'product_count': product_count,
            'doctors_count': doctor_count,
            'deals':deals,
            'schedules':schedules,
        }
        return render(request, 'home.html', context)
     else:
          messages.error(request, "Please log in first.")
          return redirect('login')


IMAGE_FIELD_TYPES = ['png','jpg','jpeg']
def new_product(request):
     if request.user.is_authenticated:
        form_data = Add_product()
        if request.method == "POST":
            form_data = Add_product(request.POST, request.FILES)
            print(f'Form Data {form_data}')
            if form_data.is_valid():
                post_data = form_data.save(commit=False)
                post_data.display_picture = request.FILES['Image']
                file_type = post_data.Image.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FIELD_TYPES:
                    return render(request, 'error.html')
                post_data.Entered_By = request.user
                post_data.save()
                messages.success(request, 'Data has been inserted successfully')
                return redirect('index')
            else:
                return render(request, ' products_add.html', {'form': form_data})
        else:
            return render(request, 'products_add.html', {'form': form_data})
     else:
            messages.error(request, "Please log in first.")
            return redirect('login')


def add_doctor(request):
     if request.user.is_authenticated:
        if request.method == "POST":
            form_data = Add_Doctor(request.POST)
            if form_data.is_valid():
                post_data = form_data.save(commit=False)
                post_data.Entered_By = request.user
                post_data.save()
                messages.success(request, 'Data has been inserted Sucesfully')
                return redirect('index')

        else:
            form_data =  Add_Doctor()

        return render(request, 'doctor_add.html', {'form': form_data})
     else:
            messages.error(request, "Please log in first.")
            return redirect('login')


def todays_appointment(request):
     if request.user.is_authenticated:
        today = datetime.now().date()
        schedules = Schedule.objects.filter(Date_Of_Schedule=today)
        context = {
            'schedules': schedules
        }
        return render(request, 'today_schedule.html', context)
     else:
            messages.error(request, "Please log in first.")
            return redirect('login')


def appointment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_data = ScheduleAppointment(request.POST)
            if form_data.is_valid():
                post_data = form_data.save(commit=False)
                post_data.Entered_By = request.user
                post_data.save()
                messages.success(request, 'Data has been inserted Sucesfully')
                return redirect('index')

        else:
            form_data =  ScheduleAppointment()

        return render(request, 'schedule_appointment.html', {'form': form_data})
    else:
            messages.error(request, "Please log in first.")
            return redirect('login')


def product_table(request):
     if request.user.is_authenticated:
        products = Products.objects.all()
        context = {'products': products}
        return render(request, 'product_table.html', context)
     else:
            messages.error(request, "Please log in first.")
            return redirect('login')


def add_deals(request):
     if request.user.is_authenticated:
        if request.method == 'POST':
            form = Add_Deals(request.POST)
            if form.is_valid():
                deal = form.save(commit=False)
                deal.Entered_By = request.user
                deal.save()
                return redirect('index')
        else:
            form = Add_Deals()
        return render(request, 'deals_add.html', {'form': form})
     else:
            messages.error(request, "Please log in first.")
            return redirect('login')
