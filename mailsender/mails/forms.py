from django import forms

class EmailForm(forms.Form):
    to = forms.EmailField()
    subject = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)