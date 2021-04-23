from django.shortcuts import render, redirect


def index(req):
    return render(req, 'index.html', {})

def login(req):
    return render(req, 'login.html', {})

def register(req):
    return render(req, 'register.html', {})

def user_info(req):
    return render(req, 'user_info.html', {})