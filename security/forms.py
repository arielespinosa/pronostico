from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from .models import AppUser


class UserAuthenticationForm(AuthenticationForm):
    username  = forms.CharField(min_length=1, label='Usuario', widget=forms.TextInput())
    password  = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(render_value=True))
    error_messages = {
        'invalid_login': _("No se reconoce la combinación de nombre de usuario y contraseña. "
                           "Note que ambos campos pueden ser sensibles a las mayúsculas."), 
        'inactive':      _("Su cuenta está inactiva. Póngase en contacto con el administrador para activarla."),
        
    }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            #print(self.user_cache)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                print(user_temp)

                if user_temp is not None:
                    if user_temp.is_active:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )
                    else:
                        try:
                            #print(self.user_cache)
                            self.confirm_login_allowed(user_temp)
                        except:
                            raise forms.ValidationError(
                                self.error_messages['inactive'],
                                code='inactive',
                                params={'username': self.username_field.verbose_name},
                            )
                else:
                    try:
                        self.confirm_login_allowed(user_temp)
                    except:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )

        return self.cleaned_data

        
class UserRegistrationForm(UserCreationForm):
    username  = forms.CharField(min_length=1, label='Nombre de usuario', widget=forms.TextInput(), error_messages={'unique': 'El usuario ya existe'})
    password1 = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(min_length=2, label='Confirmar contraseña', widget=forms.PasswordInput(render_value=True))
    email     = forms.EmailField(label='E-mail', widget=forms.TextInput())
    agree     = forms.BooleanField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    # Validar que los passwords coincidan
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    # Validar email    
    def clean_email(self):
        email_address = self.cleaned_data['email']

        if '@insmet.cu' not in email_address:
            raise forms.ValidationError('La dirección de correo debe ser del dominio insmet.cu')
        return  email_address
    

class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)


class FormAppUser(BSModalForm):
    class Meta:
        model = AppUser
        fields = '__all__'
        

    
