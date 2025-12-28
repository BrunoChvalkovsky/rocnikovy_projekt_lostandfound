from django.shortcuts import render, get_object_or_404
from .models import Post, Profile

def homepage (request):
    posts = Post.objects.all()

    return render(request, 'project/homepage.html',
                {
                        'page': 'homepage',
                        'posts': posts,
                  })
def postdetails(request, id):

    return render(request, 'project/postdetails.html',
                  {
                      'page': 'postdetails',
                  })
def createpost(request):

    return render(request, 'project/createpost.html',
                  {
                      'page': 'createpost',
                  })
def userposts(request, id):

    return render(request, 'project/userposts.html',
                  {
                      'page': 'userposts',
                  })
def myposts(request):

    return render(request, 'project/myposts.html',
                  {
                      'page': 'myposts',
                  })
def login(request):

    return render(request, 'project/login.html',
                  {
                      'page': 'login',
                  })
def signup(request):

    return render(request, 'project/signup.html',
                  {
                      'page': 'signup',
                  })