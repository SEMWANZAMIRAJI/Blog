from typing import Any
from django.views.generic import ListView, CreateView,UpdateView,DeleteView,DetailView
from .models import Feed, User,Comment
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import login
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["text"]
    template_name ='createcomment.html'
    # fields = ["text", "feed"]
    # template_name = "createcomment.html"
    # pk_url_kwarg = "pk"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """ Associate comment with the current logged in user as its author"""

        # get the id of current logged in user
        user_id = self.request.user.id

        # retrieve the user with this id
        user = User.objects.get(id=user_id)

        # add author to the post
        form.instance.author = user

        # form.instance.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #hii code inaeleza kwamba irudishe id ya post yako kwa kutumia
        context["feed"] = Feed.objects.get(id=self.kwargs["pk"])
        return context





# function based view
# class based view
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Feed
    fields = ['image', 'text']
    template_name = 'update.html'
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = self.object  # Customize context variable name if needed
    #     return context
    
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Feed
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy("login")
    
    
class Login(LoginView):
    template_name = "login.html"
    fields = ["username", "password"]
    # redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    # def get_success_url(self) -> Any:
    #     return reverse_lazy("home")
    
class Logout(LogoutView):
    next_page = reverse_lazy("home")


class HomePage(ListView):
    model = Feed
    template_name = "index.html"

    # context data
    # object_list
    # {
    #  "author": "user",
    #  "text": "text",
    #  "created_at": "date",
    #  "image": "image"
    # }


class CreateFeed(LoginRequiredMixin, CreateView):
    model = Feed
    fields = ["text", "image"]
    template_name = "create_post.html"
    success_url = reverse_lazy("home") # this return user to hom page
    login_url = reverse_lazy("login") # this return user to login page

    def form_valid(self, form):
        """ Associate post with the current logged in user as its author"""
        
        # get the id of current logged in user
        user_id = self.request.user.id
        
        # retrieve the user with this id
        user = User.objects.get(id=user_id)
        
        # add author to the post
        form.instance.author = user
        
        # form.instance.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


class FeedDetailview(DetailView):
    model = Feed
    template_name = "feeddetail.html"
    # context_object_name = "feed" # used as custom context name in template

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)  
        # get all comments for this post (feed)
        feed_id = self.kwargs["pk"]
        context["comments"] = Comment.objects.filter(feed=feed_id)
        return context


class RegisterView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'image']
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    
    # def form_valid(self, form):
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.set_password(form.cleaned_data['password'])
    #         user.save()
    #         login(self.request, user)
    #         return super().form_valid(form)
    #     else:
    #         print(form.errors)  # Print form errors to debug
    #         return self.form_invalid(form)
