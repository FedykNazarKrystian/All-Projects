from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def user_register(request):
    username = request.data['username']
    password = make_password(request.data['password'])

    user = User.objects.create(username=username, password=password)
    user.save()
    return Response({'message': 'User created successfully'})

@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.get(username=username)
    if user.check_password(password):
        refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_data(request):
    return Response({'message': 'Private data is only available with jwt'})

@api_view(['GET'])
def register_page(request):
    return render(request, 'accounts/register.html')

@api_view(['GET'])
def login_page(request):
    return render(request, 'accounts/login.html')
