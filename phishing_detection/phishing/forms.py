from django import forms

class EmailAnalysisForm(forms.Form):
    sender_email = forms.EmailField()
    email_body = forms.CharField()
    url_links = forms.CharField()
