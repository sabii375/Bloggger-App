from django.db import models
from django.contrib.auth.models import AbstractUser, User, Permission,Group
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=50)


class UserTable(AbstractUser):
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100, null=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions_user_table')
    groups = models.ManyToManyField(Group, related_name='user_groups_user_table')



class Blog(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=True)
    # date_modified = models.DateTimeField(auto_now=True, editable=True)

class Login(AbstractUser):
    
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions_login')
    groups = models.ManyToManyField(Group, related_name='user_groups_login')


    
class Signin(AbstractUser):
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions_signin')
    groups = models.ManyToManyField(Group, related_name='user_groups_signin')









