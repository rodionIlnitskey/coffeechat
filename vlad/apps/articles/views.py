from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment
from django.urls import reverse

def index(request):
    latest_comments_list = Comment.objects.all()
    return render(request, 'articles/index.html', {'latest_comments_list': latest_comments_list})

def leave_comment(request):
    Comment.objects.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:index') )
