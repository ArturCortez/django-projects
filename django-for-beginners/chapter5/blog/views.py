# blog/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView 
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from django.contrib.auth import logout

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields =['title', 'body']

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class LogoutView(View): # new
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')




