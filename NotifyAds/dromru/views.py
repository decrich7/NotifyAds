from django.contrib.auth.decorators import login_required
from .models import AdsFilter
from .forms import UserRegForm, UserLoginForm, FilterUser
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout



# переделать с использованием классоа представления




def index(request):
    return render(request, 'dromru/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('filters')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegForm()
    context = {
        'form': form
    }
    return render(request, 'dromru/register.html', context=context)


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'dromru/login.html', context=context)


def logout_user(requests):
    logout(requests)
    return redirect('login')


@login_required
def filters(request):
    filters = AdsFilter.objects.filter(users_filters=request.user)

    return render(request, 'dromru/filters.html', context={"filters": filters, 'amount_filters': len(filters)})


@login_required
def new_filter(request):
    if request.method == 'POST':
        form = FilterUser(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.users_filters = request.user
            post.save()
            return redirect('filters')
    else:
        form = FilterUser()
    context = {
        'form': form
    }
    return render(request, 'dromru/new_filter.html', context=context)


@login_required
def delete_filter(request, filter_id):
    # добавить пользовательский тег чтоюы постоянно не получать fikters
    get_filter = AdsFilter.objects.get(pk=filter_id)
    get_filter.delete()
    return redirect('filters')


@login_required
def stop_filter(request, filter_id):
    # добавить пользовательский тег чтоюы постоянно не получать filters
    get_filter = AdsFilter.objects.get(pk=filter_id)
    get_filter.default_start = False
    get_filter.save()
    return redirect('filters')



@login_required
def start_filter(request, filter_id):
    # добавить пользовательский тег чтоюы постоянно не получать filters
    get_filter = AdsFilter.objects.get(pk=filter_id)
    get_filter.default_start = True
    get_filter.save()
    return redirect('filters')

@login_required
def change_filter(request, filter_id):
    # # добавить пользовательский тег чтоюы постоянно не получать filters
    # filters = AdsFilter.objects.filter(users_filters=request.user)
    # get_filter = AdsFilter.objects.get(pk=filter_id)
    # get_filter.default_start = False
    # get_filter.save()
    return render(request, 'dromru/filters.html')
