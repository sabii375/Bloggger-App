from django.shortcuts import render, redirect
from .forms import LoginForm, SigninForm
from .models import Blog, Category
# Create your views here.
def homePage(request):
    return render(request, 'home.html')


def signinPage(request):
    if request.method=="POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    else:
        form=SigninForm()
        return render(request,'signin.html',{'form':form})
    

def loginPage(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    

def displayBlog(request):
    #Fetching all the categories
    categories = Category.objects.all()

    #Creating a dictionary to store the blogs by category
    blogByCategory={}

    for category in categories:
        #Get all the blogs from the current category
        blogs = Blog.objects.filter(Category=category)
        blogByCategory[category]=blogs

        return render(request, 'home.html',{'blogByCategory':blogByCategory})
