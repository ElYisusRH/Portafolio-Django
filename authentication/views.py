from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class SingUpView(CreateView):

    template_name="registration/singup.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("login")