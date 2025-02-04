from django.shortcuts import render
import random
import string
import secrets
from django.http import HttpResponse

# Create your views here.
def generate_password(request):
    

    password = ""
    for _ in range(9):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    return HttpResponse(password)

    

