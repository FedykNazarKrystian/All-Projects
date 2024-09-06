from django.shortcuts import render
from django.contrib.auth.models import User

def chat(request):
    users = User.objects.all()
    return render(request, 'chat/chat.html', {'users': users})

