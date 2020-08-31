from django.template.defaulttags import register


@register.filter
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def dict_get(dictionary, key_value):
    return dictionary.get(key_value, 'Nothing found')
