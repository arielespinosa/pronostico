from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .mixins import BSModalAjaxFormMixin
from . import forms



app_name = 'configuration'

def configuration(request):
    context = {
        
    }

    return render(request, 'configuration_users.html', context)

def users(request):

    groups = Group.objects.all()

    context = {
        'groups': groups
    }

    return render(request, 'configuration_users.html', context)


class GroupCreateView(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'additional/add_group.html'
    form_class = forms.FormGroup
    success_message = 'El grupo se creó satisfactoriamente.'
    success_url = reverse_lazy('configuration')

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)        

        if form.is_valid():

            print(request)
  
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


