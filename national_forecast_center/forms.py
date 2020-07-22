from django.utils.translation import activate, gettext_lazy as _
from django import forms
from .models.documents import *
from security.models import AppUser
from django.db.models import Q
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from docx import Document
from cnp import settings
from datetime import datetime, date


class FormSecundaryAuthors(forms.Form):
    authors = None

class FormAE(BSModalForm):
    class Meta:
        model  = AE
        fields = ['no','emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'no': _('No'),
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        help_texts = {
            'title': _('El título debe ser lo más describtivo posible'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
    
class FormNI(BSModalForm):
    class Meta:
        model = NI 
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        help_texts = {
            'no': _('El valor debe ser único'),
        }
        error_messages = {
            'no': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPT5(BSModalForm):
    class Meta:
        model = PT5
        fields = ['title', 'sinopsis', 'content', 'day1', 'day2', 'day3', 'day4', 'day5', 'notes', 'main_author']
        labels = {
            'title':   _('Título'),
            'sinopsis':_('Sinopsis'),
            'day1':    _('Día 1'),
            'day2':    _('Día 2'),
            'day3':    _('Día 3'),
            'day4':    _('Día 4'),
            'day5':    _('Día 5'),
            'content': _('Contenido'),
            'notes':   _('Notas'),
            'main_author': _('Author principal'),
        }
        help_texts = {
            'title': _('El valor debe ser único'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'day1': forms.Textarea(attrs={'cols': 80, 'rows': 5}), 
            'day2': forms.Textarea(attrs={'cols': 80, 'rows': 5}), 
            'day3': forms.Textarea(attrs={'cols': 80, 'rows': 5}), 
            'day4': forms.Textarea(attrs={'cols': 80, 'rows': 5}), 
            'day5': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'notes'  : forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPTM(BSModalForm):
    class Meta:
        model = PTM
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors', 'notes']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        help_texts = {
            'no': _('El valor debe ser único'),
        }
        error_messages = {
            'no': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPTHOY(BSModalForm):
    class Meta:
        model = PTHOY
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPTRD(BSModalForm):
    class Meta:
        model = PTRD
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPTT(BSModalForm):
    class Meta:
        model = PTT
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormDP10(BSModalForm):
    class Meta:
        model = DP10
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormPTTN(BSModalForm):
    class Meta:
        model = PTTN
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class FormEGT(BSModalForm):
    class Meta:
        model = EGT
        exclude = ['creation_date']

        labels = {
            'code': _('Código'),
            'emision_date_utc': _('Fecha en UTC'),
            'emision_date': _('Fecha'),
            'nombre': _('Nombre'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'notes': _('Notas'),
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }

        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },

            'authors': {
                'error': _("Pepe no está."),
            },
        }

        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    """
    def clean_authors(self):
        authors = self.cleaned_data.get('authors')

        print(authors)

        if "Pepe" not in authors:
            raise forms.ValidationError("Pepe no está")
        return authors
        """



class FormACT(BSModalForm):
    class Meta:
        model = ACT
        fields = ['emision_date', 'title', 'content', 'main_author', 'authors']
        labels = {
            'emision_date': _('Fecha'),
            'title':   _('Título'),
            'content': _('Contenido'), 
            'main_author': _('Autor principal'),  
            'authors': _('Autores secundarios'),
        }
        error_messages = {
            'title': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
    
          
class InputFileForm(forms.Form):
    file = forms.FileField()

class FormUpload(forms.Form):
    file = forms.FileField()
    filetype = None

    def __init__(self, *args, **kwargs):
        super(FormUpload, self).__init__(*args, **kwargs)

    def datestring(self, dstring):
        dstring = dstring.replace("Fecha: ", "")
        dstring = dstring.replace("Hora: ", "")
        dstring = dstring.split(".")

        h = dstring[1].strip()[:2]
        m = dstring[1].strip()[3:5]
        med = "AM" if dstring[1].count("a") > 0 or dstring[1].count("A") > 0 else "PM"

        creation = dstring[0].split("de")

        months = {
            "enero": "01",
            "febrero": "02",
            "marzo": "03",
            "abril": "04",
            "mayo": "05",
            "junio": "06",
            "julio": "07",
            "agosto": "08",
            "septiembre": "09",
            "octubre": "10",
            "noviembre": "11",
            "diciembre": "12",
        }

        date = creation[0].strip().zfill(2) + months[creation[1].strip()] + creation[2].strip().zfill(2) + h.zfill(2) + m + med
        return datetime.strptime(date, "%d%m%Y%I%M%p")

    def handle_file(self, filename, user):
        document = Document(filename)
        paragraphs = [paragraph for paragraph in document.paragraphs if paragraph.text != ""]
        
        if "PTH" in str(filename):
            data = self.proccess_pth(paragraphs, user)
            notice = PTHOY(
                emision_date=data["emision_date"],
                title=data["title"],
                content=data["content"],
                notes=data["notes"],
                main_author=data["main_author"],
            )

        elif "AE" in str(filename):
            data = self.proccess_ae(paragraphs, user)
            notice = AE(
                no=data["no"],
                emision_date=data["emision_date"],
                title=data["title"],
                content=data["content"],
                main_author=data["main_author"],
            )            

        elif "ACT" in str(filename):
            data = self.proccess_act(paragraphs)
            notice = ACT(
                emision_date=data["emision_date"],
                title=data["title"],
                phenomena=data["phenomena"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "DP10" in str(filename):
            data = self.proccess_dp10(paragraphs)
            notice = DP10(
                emision_date=data["emision_date"],
                notes=data["notes"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "EGT00" in str(filename):
            data = self.proccess_egt00(paragraphs)
            notice = EGT00(
                emision_date=data["emision_date"],
                notes=data["notes"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "EGT12" in str(filename):
            data = self.proccess_egt12(paragraphs)
            notice = EGT12(
                emision_date=data["emision_date"],
                notes=data["notes"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "P5" in str(filename):
            data = self.proccess_p5(paragraphs)
            notice = PT5(
                emision_date=data["emision_date"],
                notes=data["notes"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "PTM" in str(filename):
            data = self.proccess_ptm(paragraphs)
            notice = PTM(
                emision_date=data["emision_date"],
                title=data["title"],
                content=data["content"],
                notes=data["notes"],
                main_author=data["main_author"],
            )

        elif "PTRD" in str(filename):
            data = self.proccess_ptrd(paragraphs)
            notice = PTRD(
                emision_date=data["emision_date"],
                title=data["title"],
                content=data["content"],
                notes=data["notes"],
                main_author=data["main_author"],
            )

        elif "PTT" in str(filename) and "PTTN" not in str(filename):
            data = self.proccess_ptt(paragraphs)
            notice = PTT(
                emision_date=data["emision_date"],
                content=data["content"],
                main_author=data["main_author"],
            )

        elif "PTTN" in str(filename):
            data = self.proccess_pttn(paragraphs)
            notice = PTTN(
                emision_date=data["emision_date"],
                title=data["title"],
                content=data["content"],
                notes=data["notes"],
                main_author=data["main_author"],
            )

        else:
            # Let user know than kind of doc don't exist
            pass

        self.filetype = notice.typeof()

        notice.save(False)
        notice.authors.set(data["authors"])
        notice.save()

    def proccess_pth(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)
        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in range(len(doc_authors))]

        data = {
            "emision_date": creation_date,
            "title": paragraphs[6].text,
            "content": content,
            "notes": paragraphs[5].text,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data 

    def proccess_pth(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)
        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in range(len(doc_authors))]

        data = {
            "emision_date": creation_date,
            "title": paragraphs[6].text,
            "content": content,
            "notes": paragraphs[5].text,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data 

    def proccess_ae(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"

        no = int(paragraphs[5].text.split(".")[-1])
        creation_date = self.datestring(paragraphs[4].text)
        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in range(len(doc_authors))]

        data = {
            "no": no,
            "emision_date": creation_date,
            "title": paragraphs[6].text,
            "content": content,           
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data 

    def proccess_act(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        phenomena = Phenomena(
            name=paragraphs[6].text,
            type_of_phenomena="CT"
        )

        phenomena.save()

        data = {
            "emision_date": creation_date,
            "title": paragraphs[5].text,
            "phenomena": phenomena,
            "content": content,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data

    def proccess_dp10(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        data = {
            "emision_date": creation_date,
            "notes": paragraphs[5].text,
            "content": content,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data

    def proccess_egt00(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        data = {
            "emision_date": creation_date,
            "title": paragraphs[3].text,
            "notes": paragraphs[5].text,
            "content": content,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data

    def proccess_egt12(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        data = {
            "emision_date": creation_date,
            "title": paragraphs[3].text,
            "notes": paragraphs[5].text,
            "content": content,
            "main_author": authors[0],
            "authors": authors[1:],
        }

        return data

    def proccess_p5(self, paragraphs, user):
        return None 

    def proccess_ptm(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        return {
            "emision_date": creation_date,
            "title": paragraphs[6].text,
            "content": content,
            "notes": paragraphs[5].text,
            "main_author": authors[0],
            "authors": authors[1:],
        }

    def proccess_ptrd(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        return {
            "emision_date": creation_date,
            "title": paragraphs[7].text,
            "content": content,
            "notes": paragraphs[5].text,
            "main_author": authors[0],
            "authors": authors[1:],
        }

    def proccess_ptt(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        return {
            "emision_date": creation_date,
            "content": content,
            "main_author": authors[0],
            "authors": authors[1:],
        }

    def proccess_pttn(self, paragraphs, user):
        content = ""
        for i in range(8, len(paragraphs) - 1):
            content += paragraphs[i].text + "\n"

        creation_date = self.datestring(paragraphs[4].text)

        doc_authors = paragraphs[-1].text.split("/")
        authors = [self.find_userapp(doc_authors[i].split(".")[1].lstrip(), user.appuser.forecast_center) for i in
                   range(len(doc_authors))]

        return {
            "emision_date": creation_date,
            "title": paragraphs[7].text,
            "content": content,
            "notes": paragraphs[5].text,
            "main_author": authors[0],
            "authors": authors[1:],
        }

    def find_userapp(self, lastname, center):
        return AppUser.objects.get(
            Q(forecast_center__name=center), 
            Q(lastname1=lastname) | Q(lastname2=lastname))
        












