from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Post, Profile

def homepage (request):
    posts = Post.objects.all()
    user = request.user
    profile = user.profile
    return render(request, 'project/homepage.html',
                {
                        'page': 'homepage',
                        'posts': posts,
                        "user": user,
                        "profile": profile,
                  })

def postdetails(request, id):

    return render(request, 'project/postdetails.html',
                  {
                      'page': 'postdetails',
                  })
@login_required
def createpost(request):

    return render(request, 'project/createpost.html',
                  {
                      'page': 'createpost',
                  })

def userposts(request, id):
    posts = Post.objects.filter(owner__id=id)
    return render(request, 'project/userposts.html',
                  {
                      'page': 'userposts',
                      'posts': posts,
                  })

@login_required
def myposts(request):
    posts = Post.objects.filter(owner=request.user)

    return render(request, 'project/myposts.html',
                  {
                      'page': 'myposts',
                      'posts': posts,
                  })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            return render(request, 'project/login.html', {
                'page': 'login',
                "error": "Invalid username or password"
            })
    return render(request, 'project/login.html', {'page': 'login'})
def signup(request):

    return render(request, 'project/signup.html',
                  {
                      'page': 'signup',
                  })
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("login")