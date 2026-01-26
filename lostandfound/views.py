from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Profile
from io import BytesIO
import uuid
from django.core.files.base import ContentFile
from PIL import Image

from pillow_heif import register_heif_opener
register_heif_opener()

def homepage(request):
    posts = Post.objects.filter(is_solved=False).exclude(owner=request.user) if request.user.is_authenticated else Post.objects.filter(is_solved=False)
    posts = posts.order_by('-id')
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    return render(request, 'project/homepage.html',
                {
                        'posts': posts,
                        "profile": profile,
                  })

def postdetails(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    if request.method == "POST" and request.user == post.owner:
        post.is_solved = not post.is_solved
        post.save()
        if "delete" in request.POST:
            if post.image:
                post.image.delete(save=False)
            post.delete()
            return redirect("myposts")

        return redirect("postdetails", id=post.id)
    return render(request, 'project/postdetails.html',
                  {
                      'post': post,
                      'profile': profile
                  })
@login_required
def createpost(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    
    if request.method == "POST":
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        image = request.FILES.get("image")

        if not image:
            return render(request, "project/createpost.html", {
                "error": "Image is required.",
                "title": title,
                "description": description,
            })

        try:
            img = Image.open(image)
            img = img.convert("RGB")

            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=85)
            buffer.seek(0)

            filename = f"{uuid.uuid4()}.jpg"
            jpg_image = ContentFile(buffer.read(), name=filename)
        except Exception:
            return render(request, "project/createpost.html", {
                "error": "Invalid or unsupported image file.",
                "title": title,
                "description": description,
            })

        Post.objects.create(
            owner=request.user,
            title=title,
            description=description,
            image=jpg_image,
        )

        return redirect("myposts")

    return render(request, "project/createpost.html",{
                      "profile": profile,
    })


def userposts(request, id):
    posts = Post.objects.filter(owner__id=id)
    posts = posts.order_by('-id')
    viewed_user = User.objects.get(id=id)
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    return render(request, 'project/userposts.html',
                  {
                      'posts': posts,
                      'profile': profile,
                      'viewed_user': viewed_user
                  })

@login_required
def myposts(request):
    posts = Post.objects.filter(owner=request.user)
    posts = posts.order_by('-id')
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    return render(request, 'project/myposts.html',
                  {
                      'posts': posts,
                      'profile': profile
                  })

def login_view(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("myposts")
        else:
            return render(request, 'project/login.html', {
                "error": "Invalid username or password"
            })
    return render(request, 'project/login.html', {
        "profile": profile
    })

def signup(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            contact = request.POST.get("contact")
            name = request.POST.get("name")

            user = User.objects.create_user(username=username, password=password)
            
            user.profile.name = name
            user.profile.contact = contact
            user.profile.save()

            return redirect("login")
    return render(request, 'project/signup.html',
                  {
                      "profile": profile
                  })

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("login")