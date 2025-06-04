from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ContactForm
from accounts.models import Post


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request,"registration/register.html", {'form':form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        con = ContactForm()
    return render(request,'registration/contact.html',{'form':con})

def allpost(request):
    post = Post.objects
    return render(request,"posts/list.html",{'title':"All Posts", 'post':post})

def detail(request, blog_id):
    detail = get_object_or_404(Post, pk=blog_id)
    return render(request,"posts/details.html",{'title':detail.title, 'post':detail})