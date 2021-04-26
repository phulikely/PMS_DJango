from django.shortcuts import render, redirect
from login.models import User


def index(req):
    return render(req, 'index.html', {})

def login(req):
    if req.method == "POST":
        try:
            user_detail = User.objects.get(username=req.POST['username'], password=req.POST['password'])
            # print(user_detail.__dict__)
            # print(user_detail.username)
            req.session['username'] = user_detail.username
            # return user_info(req)
            return redirect('user_infooo')
        except :
            context = {'msg': 'Invalid email or password!'}
            return render(req, 'login.html', context)
    return render(req, 'login.html', {})

def register(req):
    if req.method == "POST":
        try:
            if User.objects.filter(username=req.POST['username']).exists():
                context = {'msg': 'User Name already existed!'}
                return render(req, 'register.html', context)
            elif req.POST['password'] != req.POST['re-password']:
                context = {'msg': 'Passwords do not match!'}
                return render(req, 'register.html', context)
            user = User(username = req.POST['username'], password = req.POST['password'])
            user.save()
            return redirect('loginnn')
        except :
            context = {'msg': 'Something happened. Please check again!'}         
    return render(req, 'register.html', {})

def user_info(req):
    return render(req, 'user_info.html', {})