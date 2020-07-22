from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import Group

from bootstrap_modal_forms.forms import BSModalForm


class FormGroup(BSModalForm):
    class Meta:
        model  = Group
        fields = '__all__'
        """
        labels = {
            'title':   _('Título'),
            'content': _('Contenido'),
            'notes':   _('Notas'),   
            'author2': _('Segundo autor'),
        }
        help_texts = {
            'title': _('El debe ser lo más describtivo posible'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'notes'  : forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        """













