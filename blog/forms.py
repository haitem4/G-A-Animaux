from django import forms


class AdoptForm(forms.Form):
    nom = forms.CharField(name='nom', max_length=100)
