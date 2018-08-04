from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm
from .models import Blog

# Create your views here.


def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            print("secces")
            return render(request,'home.html')

    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})



def createblog(request):
    if request.method == 'GET':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = BlogForm()

    return render(request,'create.html', {'form': form})


def viewblog(request):
    blog = Blog.objects.filter(user=request.user)
    print(blog)
    # if blog.user == request.user:
    #     print("true")
    # else:
    #     print("false")
    return render(request,'view.html',{'blogs':blog})


def updateblog(request, pk):
        blog = get_object_or_404(Blog, pk=pk)

        if request.method == 'POST':
            print("if part:")
            form = BlogForm(request.POST,instance=blog)
            if form.is_valid():
                form.save()
                return redirect('view',permanent=True)
        else:
            print("else part")
            form = BlogForm(instance=blog)
            return render(request, 'update.html',{"form":form})


def deleteblog(request, pk):
    blog =  get_object_or_404(Blog, pk=pk)
    print("deleteblogenrty")
    if request.method == 'POST':
        blog.delete()
        return redirect('view',permanent=True)

    else:
        form = BlogForm(instance=blog)
        return render(request,'delete.html',{'form':form})