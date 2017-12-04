from django import forms

class AddMusicForm(forms.Form):
    sid = forms.CharField(required=True,max_length=10,min_length=10)
    aid = forms.CharField(required=True,max_length=10,min_length=10)
    gid = forms.CharField(required=True,max_length=10,min_length=10)
    name = forms.CharField(required=True,max_length=50,min_length=0,help_text='Max 50 Char')
    releaseDate = forms.CharField(required=True)
    numDownloads = forms.CharField(required=True)
    numLicense = forms.CharField(required=True)
