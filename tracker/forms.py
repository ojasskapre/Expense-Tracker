from django import forms


class AddDetailForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    payment_method = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    amount = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    spent_on = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
