from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import (
    LoginForm, RegisterForm, EditProfileForm, UsersAdressesAddForm, 
    EditUsersAdressesForm, UsersContactPreferencesForm)
from django.contrib import messages

from .models import UsersContactPreferences, UsersAdresses
from ecoshop.models import Goods
from django.contrib.auth.models import User

from django .contrib.auth.decorators import login_required

from django.conf import settings


def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Вы успешно зарегистрировались под ником " + user)
                return redirect('accounts:login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.info(request, 'Имя пользователя или пароль введены неверно.')
        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url = 'accounts:login')
def logout_view(request):
    logout(request)
    #request.user == Anon user
    return redirect('accounts:login')

#FIXME: при регистрации или логине через гугл пересылает не на /home/ , а на /accounts/login
#ну короче чето нужно с этим делать, а вот че - не знаю
@login_required(login_url = 'accounts:login')
def home(request):
    return render(request, 'accounts/home_pages/home.html')


@login_required(login_url = 'accounts:login')
def fav_goods(request):
    fav_goods = Goods.published.filter(likes = request.user)
    return render(request, 'accounts/home_pages/favourities_goods.html', {'goods':fav_goods})

@login_required(login_url = 'accounts:login')
def my_info(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно сменили данные.')
            return redirect('accounts:my_info')
        else:
            messages.warning(request, 'Произошла ошибка, попробуйте позже или напишите нам.')
    else:
        form = EditProfileForm(instance = request.user)
        context = {'form':form}
        return render(request, 'accounts/home_pages/my_info.html', context)


@login_required(login_url = 'accounts:login')
def profile_adress(request):
    adresses = UsersAdresses.objects.filter(user_id = request.user.id)
    context = {'adresses':adresses}
    return render(request, 'accounts/home_pages/adress.html', context)


@login_required(login_url = 'accounts:login')
def add_adress(request):
    form = UsersAdressesAddForm()
    if request.method == "POST":
        form = UsersAdressesAddForm(request.POST)
        if form.is_valid():
            add_adress = form.save(commit = False) 
            add_adress.user = request.user
            add_adress.save()
            return redirect('accounts:adresses')
        else:
            messages.warning(request, 'Произошла ошибка, попробуйте позже или напишите нам.')
    context = {'form':form}
    return render(request, 'accounts/home_pages/add_adress.html', context)


@login_required(login_url = 'accounts:login')
def change_adress(request, adress_id):
    default_adress_values = UsersAdresses.objects.filter(user_id = request.user.id).values_list('default_adress', flat = True)
    adress = UsersAdresses.objects.get(id = adress_id)
    form = EditUsersAdressesForm(instance = adress)
    if request.method == "POST":
        # get_or_create
        form = EditUsersAdressesForm(request.POST, instance = adress)
        if form.is_valid():
            if True in default_adress_values:
                if request.POST.get('default_adress'):
                    messages.info(request, 'Вы обновили адрес по умолчанию')
                    UsersAdresses.objects.filter(user_id = request.user.id).update(default_adress = False)
                    form.save()
                    messages.success(request, 'Вы успешно сменили данные.')
                    return redirect('accounts:adresses')
                else:
                    form.save()
                    messages.success(request, 'Вы успешно сменили данные.')
                    return redirect('accounts:adresses')
            else:
                form.save()
                messages.success(request, 'Вы успешно сменили данные.')
                return redirect('accounts:adresses')
        else:
            messages.warning(request, 'Произошла ошибка, попробуйте позже или напишите нам.')
    context = {'form':form}
    return render(request, 'accounts/home_pages/change_adress.html', context)


@login_required(login_url = 'accounts:login')
def delete_adress(request, adress_id):
    UsersAdresses.objects.get(id = adress_id).delete()
    return redirect('accounts:adresses')


@login_required(login_url = 'accounts:login')
def change_contacts_preferences(request):
    contact = UsersContactPreferences.objects.get(user_id = request.user.id)
    form = UsersContactPreferencesForm(instance = contact)
    if request.method == "POST":
        # get_or_create
        form = UsersContactPreferencesForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно сменили данные.')
            return redirect('accounts:contacts')
        else:
            messages.warning(request, 'Произошла ошибка, попробуйте позже или напишите нам.')
    context = {'form':form}
    return render(request, 'accounts/home_pages/contacts.html', context)
