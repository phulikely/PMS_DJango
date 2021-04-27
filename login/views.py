from django.shortcuts import render, redirect
from login.models import User, User_Detail, User_Role, Project, Project_Detail


def index(req):
    return render(req, 'index.html', {})

def login(req):
    if req.method == "POST":
        try:
            user_detail = User.objects.get(username=req.POST['username'], password=req.POST['password'])
            # print(user_detail.__dict__)
            # print(user_detail.username)
            req.session['user_id'] = user_detail.user_id
            req.session['username'] = user_detail.username
            # context = {'username': 'VietLaTao', 'email':'test_email@gmail.com'}
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
    username = req.session['username']
    id = req.session['user_id']
    user_info = User_Detail.objects.get(user_id=id)
    #print(user_info.__dict__)
    email = user_info.email
    full_name = user_info.fullname
    phone = user_info.phone
    dept = user_info.dept
    address = user_info.address
    birthday = user_info.birthday
    joinday = user_info.joinday
    context = {'username': username, 
                'email': email,
                'full_name': full_name,
                'phone': phone,
                'dept': dept,
                'address': address,
                'birthday': birthday,
                'joinday': joinday,
                'id': id
                }
    #print(context['username'])
    return render(req, 'user_info.html', context)