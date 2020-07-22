from datetime import date
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _

today = date.today()
print(today.strftime("%B %Y"))

activate('ru')

subject = _("Topics for {date}").format(date=today.strftime("%B %Y"))
print(subject)