from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def my_events(request):
    return HttpResponse('hello world')

    