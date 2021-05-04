from django.shortcuts import render, redirect
from login.models import User, Project, Project_Detail
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(req):
    return render(req, 'index.html', {})

def login(req):
    if req.method == "POST":
        try:
            user = User.objects.get(username=req.POST['username'], password=req.POST['password'])
            req.session['user_id'] = user.user_id
            req.session['username'] = user.username
            # context = {'username': 'VietLaTao', 'email':'test_email@gmail.com'}    
            return redirect('user_infooo')
            #return render(req, 'user_info.html', context)
        except :
            context = {'msg': 'Invalid email or password!'}
            return render(req, 'login.html', context)
    return render(req, 'login.html', {})

def register(req):
    if req.method == "POST" and req.FILES['image']:
        try:
            if User.objects.filter(username=req.POST['username']).exists():
                context = {'msg': 'User Name already existed!'}
                return render(req, 'register.html', context)
            elif req.POST['password'] != req.POST['re-password']:
                context = {'msg': 'Passwords do not match!'}
                return render(req, 'register.html', context)
            myfile = req.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            user = User(username = req.POST['username'], 
                        password = req.POST['password'],
                        role = req.POST['role'],
                        sex = req.POST['sex'],
                        email = req.POST['email'],
                        fullname = req.POST['full_name'],
                        phone = req.POST['phone'],
                        dept = req.POST['dept'],
                        address = req.POST['address'],
                        birthday = req.POST['birthday'],
                        joinday = req.POST['join_day'],
                        image=f"img/{filename}",
                        )
            user.save()
            return redirect('loginnn')
        except:
            context = {'msg': 'Something happened. Please check again!'}         
    return render(req, 'register.html', {})


def user_info(req):
    username = req.session['username']
    id = req.session['user_id']
    user_info = User.objects.get(user_id=id)
    email = user_info.email
    full_name = user_info.fullname
    phone = user_info.phone
    dept = user_info.dept
    address = user_info.address
    birthday = user_info.birthday
    joinday = user_info.joinday
    sex = user_info.sex
    role = user_info.role
    image = user_info.image
    context = {'username': username, 
                'email': email,
                'full_name': full_name,
                'phone': phone,
                'dept': dept,
                'address': address,
                'birthday': birthday,
                'joinday': joinday,
                'id': id,
                'sex': sex,
                'role': role,
                'image': image,
                }
    print(context['role'])
    return render(req, 'user_info.html', context)

def logout_view(req):
    logout(req)
    return redirect('loginnn')