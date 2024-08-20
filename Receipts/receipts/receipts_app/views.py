from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegisterForm, ReceiptForm
from .models import Receipt


def index(request):
    receipts = Receipt.objects.all()
    return render(request, 'receipts_app/index.html', {'receipts': receipts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegisterForm()
        return render(request, 'receipts_app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'receipts_app/login.html', {'form': form})
@login_required
def add_receipts(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt.author = request.user
            form.save()
            return redirect('index')
    else:
        form = ReceiptForm()
    return render(request, 'receipts_app/add_receipts.html', {'form': form})

@login_required
def edit_receipts(request, id):
    receipt_just = get_object_or_404(Receipt, id=id)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt_just)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReceiptForm(instance=receipt_just)
    return render(request, 'receipts_app/edit_receipts.html', {'form': form})

def receipt(request, id):
    receipt_list = get_object_or_404(Receipt, id=id)
    return render(request, 'receipts_app/receipt.html', {'receipt_list': receipt_list})

def logout_user(request):
    logout(request)
    return redirect('index')

