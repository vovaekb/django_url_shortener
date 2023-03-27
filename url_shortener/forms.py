from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(max_length=200, label='URL')

    class Meta:
        fields = ['url']