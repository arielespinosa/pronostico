# Python library
import json

# Django framework
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# Thirds projects
# bootstrap_modal_forms
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

# Django-notifications-hq
from django.db.models.signals import post_save
from notifications.signals import notify

# CNP Project
# Security APP
from security.models import AppUser

# This App
from . import forms
from .mixins import BSModalAjaxFormMixin
from .models.documents import *
from .process_docx import handle_docx_file


from datetime import date
from django.utils.translation import activate, get_language
from django.utils.translation import ugettext
from cnp import settings
import os

app_name = 'national_forecast_center'

def forecast(request):
    """
    today = date.today()
    print("\n",today.strftime("%B %Y"))
    activate('en')
    print(get_language())
    print(ugettext("Hello"))
    activate('zh-cn')
    print(get_language())
    print(ugettext("Hello"))
    subject = _("Topics for {date}").format(date=today.strftime("%B %Y"))
    print(subject, "\n")
    """

    all_documents = list()
    all_documents.extend(AE.objects.all())
    all_documents.extend(NI.objects.all())
    all_documents.extend(PT5.objects.all())
    all_documents.extend(PTM.objects.all())
    all_documents.extend(PTHOY.objects.all())
    all_documents.extend(PTRD.objects.all())
    all_documents.extend(PTT.objects.all())
    all_documents.extend(DP10.objects.all())
    all_documents.extend(PTTN.objects.all())
    all_documents.extend(EGT.objects.all())
    all_documents.extend(ACT.objects.all())

    notifications = request.user.notifications.unread()[:5]
    paginator = Paginator(all_documents, 10)
    page = request.GET.get('page')
    
    context = {        
        'documents_issues': None,
        'notifications':notifications,
        'form':forms.InputFileForm(),
        }

    if paginator.count > 0:
        context['documents_issues'] = paginator.get_page(page)

    return render(request, 'forecast.html', context)

def notifications(request):    
    response = HttpResponse(content_type="cnp/reports" )
    return response

def reports(request):    
    response = HttpResponse(content_type="cnp/reports" )
    return response

def documents(request):
    response = HttpResponse(content_type="cnp/reports" )
    return response

def upload_file(request):
    if request.method == 'POST':
        form = forms.InputFileForm(request.POST, request.FILES)

        if form.is_valid():

            data = handle_docx_file(request)
            print(data)

            if data:  

                return HttpResponseRedirect("/cnp")
    else:
        form = forms.InputFileForm()
    return render(request, 'forecast.html', {'form': form})


class UploadFileView(FormView):
    '''
    Esta vista sube un archivo al servidor
    '''
    template_name = "upload_file.html"
    form_class = forms.FormUpload
    success_url = '/cnp'
 
    def get(self, request, *args, **kwargs):

        data = {'form': self.form_class}

        return render(request, self.template_name, data)
 
    def post(self, request, *args, **kwargs):
        form = forms.FormUpload(request.POST, request.FILES)

        if form.is_valid():
            if 'file' in request.FILES:
                file = request.FILES['file']      
                form.handle_file(file, request.user)
                self.savefile(file)

                # Emitir aqui una notificacion
                center = self.request.user.appuser.forecast_center
                verb = '{} emitió un {}.'.format(center, form.filetype)
                notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)

                return self.form_valid(form, **kwargs)
            else:
                return self.form_invalid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def savefile(self, file):
        with open(os.path.join(settings.MEDIA_FILES, file.name), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

class NoticeListView(ListView):
    template_name = 'forecast.html'

    def get_context_data(self, *args, **kwargs):

         context = super(NoticeListView, self).get_context_data(**kwargs)
         context['ae'] = AE.objects.all()
         context['act'] = ACT.objects.all()

         return context


class DocumentCreateView(BSModalAjaxFormMixin, BSModalCreateView):
    
    def form_valid(self, form):
        if form.instance.main_author is None:                             
            form.instance.main_author = self.request.user.appuser 
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        form.fields['main_author'].queryset = AppUser.objects.filter(forecast_center=request.user.appuser.forecast_center).exclude(id=request.user.appuser.id)
        form.fields['authors'].queryset = form.fields['main_author'].queryset
        return render(request, self.template_name, {'form':form})

# ACT CRUD
class ACTCreateView(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'additional/add_act.html'
    form_class = forms.FormACT
    success_message = 'El ACT se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def form_valid(self, form):                 
        form.instance.author1 = self.request.user.appuser
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        form.fields['main_author'].queryset = AppUser.objects.filter(forecast_center=request.user.appuser.forecast_center).exclude(id=request.user.appuser.id)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un ACT.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
class ACTReadView(BSModalReadView):
    model = ACT
    template_name = 'additional/view_act.html'

class ACTUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = ACT
    template_name = 'additional/update_act.html'
    form_class = forms.FormACT
    success_message = 'El ACT fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class ACTDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = ACT
    template_name = 'additional/delete_element.html'
    success_message = 'El ACT fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class ACTListView(ListView):
    model = ACT
    template_name = 'act_listview.html'
    context_object_name = 'act'

# EGT00 CRUD
class EGTCreateView(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'additional/add_egt.html'
    form_class = forms.FormEGT
    success_message = 'El EGT se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def form_valid(self, form):                 
        form.instance.main_author = self.request.user.appuser
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        form.fields['main_author'].queryset = AppUser.objects.filter(forecast_center=request.user.appuser.forecast_center)
        form.fields['authors'].queryset = AppUser.objects.filter(forecast_center=request.user.appuser.forecast_center).exclude(id=request.user.appuser.id)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un EGT.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user, action_object=form.instance)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
class EGTReadView(BSModalReadView):
    model = EGT
    template_name = 'additional/view_egt.html'

class EGTUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = EGT
    template_name = 'additional/update_egt.html'
    form_class = forms.FormEGT
    success_message = 'El EGT fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class EGTDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = EGT
    template_name = 'additional/delete_element.html'
    success_message = 'El EGT fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class EGTListView(ListView):
    model = EGT
    template_name = 'egt00_listview.html'
    context_object_name = 'egt00'


# AE CRUD
class AECreateView(DocumentCreateView):
    template_name = 'additional/add_special_notice.html'
    form_class = forms.FormAE    
    success_message = 'El aviso especial se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un AE.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
class AEReadView(BSModalReadView):
    model = AE
    template_name = 'additional/view_special_notice.html'

class AEUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = AE
    template_name = 'additional/update_special_notice.html'
    form_class = forms.FormAE
    success_message = 'El aviso especial fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class AEDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = AE
    template_name = 'additional/delete_element.html'
    success_message = 'El aviso especial fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class AEListView(ListView):
    model = AE
    template_name = 'special_notice_listview.html'
    context_object_name = 'special_notice'
   
# NI CRUD
class NICreateView(DocumentCreateView):
    template_name = 'additional/add_meteorological_notice.html'
    form_class = forms.FormNI
    success_message = 'La nota meteorológica se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = 'El {} emitió una NM.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class NIReadView(BSModalReadView):
    model = NI
    template_name = 'additional/view_meteorological_notice.html'

class NIUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = NI
    template_name = 'additional/update_meteorological_notice.html'
    form_class = forms.FormNI
    success_message = 'La nota meteorológica fue modificada satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class NIDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = NI
    template_name = 'additional/delete_element.html'
    success_message = 'La nota meteorológica fue eliminada satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PT5 CRUD
class PT5CreateView(DocumentCreateView):
    template_name = 'additional/add_pt5.html'
    form_class = forms.FormPT5
    success_message = 'El PT5 se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def get(self, request, *args, **kwargs):
        last_pt5 = PT5.objects.last()
        _initial = {
            'day1': last_pt5.day2,
            'day2': last_pt5.day3,
            'day3': last_pt5.day4,
            'day4': last_pt5.day5,
        }

        form = self.form_class(initial=_initial)
        form.fields['main_author'].queryset = AppUser.objects.filter(forecast_center=request.user.appuser.forecast_center).exclude(id=request.user.appuser.id)

        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PT5.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)
            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PT5ReadView(BSModalReadView):
    model = PT5
    template_name = 'additional/view_pt5.html'

class PT5UpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PT5
    template_name = 'additional/update_pt5.html'
    form_class = forms.FormPT5
    success_message = 'El PT5 fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class PT5DeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PT5
    template_name = 'additional/delete_element.html'
    success_message = 'El PT5 fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PTM CRUD
class PTMCreateView(DocumentCreateView):
    template_name = 'additional/add_ptm.html'
    form_class = forms.FormPTM
    success_message = 'El PTM se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PTM.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PTMReadView(BSModalReadView):
    model = PTM
    template_name = 'additional/view_ptm.html'

class PTMUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PTM
    template_name = 'additional/update_ptm.html'
    form_class = forms.FormPTM
    success_message = 'El PTM fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class PTMDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PTM
    template_name = 'additional/delete_element.html'
    success_message = 'El PTM fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PTHOY CRUD
class PTHOYCreateView(DocumentCreateView):
    template_name = 'additional/add_pthoy.html'
    form_class = forms.FormPTHOY
    success_message = 'El PTHOY se emitió satisfactoriamente'
    success_url = reverse_lazy('forecast')
    
    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)    

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PTHOY.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)              
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PTHOYReadView(BSModalReadView):
    model = PTHOY
    template_name = 'additional/view_pthoy.html'

class PTHOYUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PTHOY
    template_name = 'additional/update_pthoy.html'
    form_class = forms.FormPTHOY
    success_message = 'El PTHOY fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class PTHOYDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PTHOY
    template_name = 'additional/delete_element.html'
    success_message = 'El PTHOY fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PTRD CRUD 
class PTRDCreateView(DocumentCreateView):
    template_name = 'additional/add_ptrd.html'
    form_class = forms.FormPTRD
    success_message = 'El PTRD se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PTRD.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PTRDReadView(BSModalReadView):
    model = PTRD
    template_name = 'additional/view_ptrd.html'

class PTRDUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PTRD
    template_name = 'additional/update_ptrd.html'
    form_class = forms.FormPTRD
    success_message = 'El PTRD fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')
    error_message = 'No tiene permisos para modificar el PTRD.'

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        
        if self.model.author1 == self.request.user.appuser or self.model.main_author == request.user.appuser:
            return render(request, self.template_name, {'form':form})
        else:
            return super().form_invalid(form)

class PTRDDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PTRD
    template_name = 'additional/delete_element.html'
    success_message = 'El PTRD fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PTT CRUD
class PTTCreateView(DocumentCreateView):
    template_name = 'additional/add_ptt.html'
    form_class = forms.FormPTT
    success_message = 'El PTT se emitió satisfactoriamente.'
    success_url = reverse_lazy('forecast')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PTT.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PTTReadView(BSModalReadView):
    model = PTT
    template_name = 'additional/view_ptt.html'

class PTTUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PTT
    template_name = 'additional/update_ptt.html'
    form_class = forms.FormPTT
    success_message = 'El PTT fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class PTTDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PTT
    template_name = 'additional/delete_element.html'
    success_message = 'El PTT fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# DP10 CRUD
class DP10CreateView(DocumentCreateView):
    template_name = 'additional/add_dp10.html'
    form_class = forms.FormDP10
    success_message = 'El DP10 se emitió satisfactoriamente'
    success_url = reverse_lazy('forecast')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)    

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un DP10.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)              
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class DP10ReadView(BSModalReadView):
    model = DP10
    template_name = 'additional/view_dp10.html'

class DP10UpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = DP10
    template_name = 'additional/update_dp10.html'
    form_class = forms.FormDP10
    success_message = 'El DP10 fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class DP10DeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = DP10
    template_name = 'additional/delete_element.html'
    success_message = 'El DP10 fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

# PTTN CRUD
class PTTNCreateView(DocumentCreateView):
    template_name = 'additional/add_pttn.html'
    form_class = forms.FormPTTN
    success_message = 'El PTTN se emitió satisfactoriamente'
    success_url = reverse_lazy('forecast')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)    

        if form.is_valid():
            # Emitir aqui una notificacion
            center = self.request.user.appuser.forecast_center
            verb = '{} emitió un PTTN.'.format(center)
            notify.send(self.request.user, recipient=User.objects.all(), verb=verb, target=self.request.user)             
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PTTNReadView(BSModalReadView):
    model = PTTN
    template_name = 'additional/view_pttn.html'

class PTTNUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = PTTN
    template_name = 'additional/update_pttn.html'
    form_class = forms.FormPTTN
    success_message = 'El PTTN fue modificado satisfactoriamente.'
    success_url = reverse_lazy('forecast')

class PTTNDeleteView(BSModalAjaxFormMixin, BSModalDeleteView):
    model = PTTN
    template_name = 'additional/delete_element.html'
    success_message = 'El PTTN fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('forecast')
   