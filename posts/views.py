from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.

from datetime import datetime
from posts.forms import PostForm
from posts.models import Post

import json


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    ordering = ("-created")
    paginate_by = 30
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    queryset = Post.objects.all()
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    success_url = reverse_lazy("posts:feed")
    form_class = PostForm

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


@login_required
def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("posts:feed")
    else:
        form = PostForm()
    return render(
        request=request,
        template_name="posts/new.html",
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
