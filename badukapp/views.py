from django.shortcuts import render
from sgfmill import sgf
from .models import Post

def create_map(request):
    if request.method=="POST":
        post = Post()
        print(request.POST)
        post.path = request.FILES['image']
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.author = request.POST['author']
        post.save()
        posts = Post.objects.all().order_by('-created_date')
        return render(request, 'badukapp/index.html', {'posts': posts})
    else:
        return render(request, 'badukapp/post_list.html', {})

def home(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'badukapp/index.html', {'posts': posts})
