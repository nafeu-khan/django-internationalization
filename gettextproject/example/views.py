from django.shortcuts import render
from django.utils.translation import gettext as _,activate
# Create your views here.

def test (req):
    activate('bn')
    trans={
        'hello': _('hello'),
        'people': _('people')
    }
    return render(req,'html/home.html',trans)