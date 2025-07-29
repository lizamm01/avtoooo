from django import  forms

from avto.models import Autosalon


class AutoSalonForms(forms.ModelForm):
    class Meta:
        model = Autosalon
        fields = ['title', 'context', 'email', 'phone', 'address']
