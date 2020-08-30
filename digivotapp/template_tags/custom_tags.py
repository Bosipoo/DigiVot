from django import template
from django.template.defaulttags import register
from ..models import ManagerUserR 
from ..models import ElectionType 
from ..models import VoterReg 
from ..models import PoliticalParty,PoliticalCandidate


register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})


# @register.filter(name='placeholder')
# def placeholder(value, token):
#     value.field.widget.attrs["placeholder"] = token
#     return value


@register.filter
def dict_get(dictionary, key_value):
    return dictionary.get(key_value, 'Nothing found')
