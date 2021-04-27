from django.db import models

# class Account(models.Model):
#     # id = models.IntegerField(max_length=5)
#     name = models.CharField(max_length=50)
#     initial_balance = models.DecimalField(max_digits=10, decimal_places=3)
#     type = models.CharField(max_length=3)
#     create_on = models.DateTimeField()
#     notes = models.CharField(max_length=250)

# class Category(models.Model):
#     # id = models.IntegerField(max_length=5)
#     name = models.CharField(max_length=50)
#     icon = models.FileField(upload_to='icon/')      #Mình sẽ tạo thêm 1 folder icon để chứa những file icon được upload 
#     budget = models.DecimalField(max_digits=10, decimal_places=3)

# class Ledger(models.Model):
#     key = models.IntegerField(primary_key = True)
#     amount = models.DecimalField(max_digits=10, decimal_places=3)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, max_length=5)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=5)
#     transaction_type = models.CharField(max_length=3)
#     payee = models.CharField(max_length=50)
#     transfer_to = models.CharField(max_length=50)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)


class User_Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=5)


class User_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=6)
    email = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    dept = models.CharField(max_length=3)
    address = models.CharField(max_length=15)
    birthday = models.DateField()
    joinday = models.DateField()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=20)
    bug = models.IntegerField()


class Project_Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    startdate = models.DateField()
    enddate = models.DateField()
    customer_lang = models.CharField(max_length=3)
    project_tech = models.CharField(max_length=20)
    description = models.CharField(max_length=200)