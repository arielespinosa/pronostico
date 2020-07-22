from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from . import forms
from .models import AppUser
from .mixins import AjaxFormMixin, BSModalAjaxFormMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from django.contrib.auth.models import User
import time

from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')  

def signup_user_view(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST, instance=User(is_active=False))

        if form.is_valid():
            #new_user = form.cleaned_data
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.success(request, 'Account created for {{username}}!')  
            return redirect('/')
    else:
        form = forms.UserRegistrationForm() 
    
    return render(request, 'signup.html', {'form':form})



class AppUserProfile(DetailView):
    template_name = "user_profile.html"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(AppUser, id=id)

# -----------------------------------------
class AppUserUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = AppUser
    template_name = 'additional/update_appuser.html'
    form_class = forms.FormAppUser
    success_message = 'Su información personal fue modificada satisfactoriamente.'
    #success_url = reverse_lazy('forecast')

# -----------------------------------------
class AppLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = forms.UserAuthenticationForm

# -----------------------------------------
class JoinFormView(AjaxFormMixin, CreateView):
    model = User
    fields = ['username', 'password']
    template_name  = 'ajax.html'
    success_url = '/form-success/'











