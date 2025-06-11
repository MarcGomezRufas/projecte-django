from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from .models import Post, Autors, Tag
# Create your views here.

def index(request):
    try:
        posts = Post.objects.order_by("-data")[:3]
        return render(request, "blog/index.html", {"posts": posts})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

# def index(request):
#     return render(request, "blog/index.html")

def posts(request):
    try:
        posts = Post.objects.all()
        return render(request, "blog/posts.html", {"posts": posts})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def post_detall(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, "blog/post_detall.html", {"post": post})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def autors(request):
    try:
        autors = Autors.objects.all()
        return render(request, "blog/autors.html", {"autors": autors})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def autors_detall(request, autors_id):
    try:
        autor = Autors.objects.get(id=autors_id)
        return render(request, "blog/autors_detall.html", {"autor": autor})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def tags(request):
    try:
        tags = Tag.objects.all()
        return render(request, "blog/tags.html", {"tags": tags})
        # return render(request, "blog/tags.html")
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def tags_posts(request, tags_id):
    try:
        tag = Tag.objects.get(id=tags_id)
        return render(request, "blog/tags_posts.html", {"tag": tag})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)