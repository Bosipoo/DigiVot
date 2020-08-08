from django import forms
from .models import VoterReg

# class PinForm(forms.Form):
#     pin = forms.CharField(label='PIN',max_length=100)
#     # def clean(self):
#     #     data = super(PinForm,self).clean()
#     #     pin = cleaned_data.get("pin")
#     #     try:
#     #         p = AdminUserR.objects.get(id=Pin)
#     #     except AdminUserR.DoesNotExist:
#     #         raise forms.ValidationError("User does not exist.")



