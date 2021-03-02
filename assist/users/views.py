from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def registration_page(request):
    '''Renders the registration page'''
    # return HttpResponse('hello')
    return render(request, 'users/register.html')


def register_user(request):
    '''Saves a new user'''
    # create these variables if the form is sent sucessfully
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    # check if the user exists, and notify the user if it does
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'message': 'Sorry, that username is already taken'})

    # ensure the password is at least 8 characters long
    if len(password) < 8:
        return render(request, 'users/register.html', {'message': 'Passwords must be at least 8 characters long'})

    # create the user with their username and password
    user = User.objects.create_user(username=username, password=password)
    return HttpResponse('ok')
