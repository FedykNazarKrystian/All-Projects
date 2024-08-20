from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from django.contrib.auth.models import User
from django.utils import timezone

def index(request):
    context = Articles.objects.all()
    return render(request, 'newsapp/index.html', {'context': context})

def about(request):
    context = Articles.objects.all()
    return render(request, 'newsapp/about.html', {'context': context})

@login_required()
def add_news(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('about')
    else:
        form = ArticleForm()
    return render(request, 'newsapp/add_news.html', {"form": form})

def register(request):
    if request.method == "POST":
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'newsapp/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('about')
    else:
        form = AuthenticationForm()
    return render(request, 'newsapp/login.html', {'form': form})
def edit_news(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.user != article.author:
        return redirect('about')
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'newsapp/edit_news.html', {'form': form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('about')
