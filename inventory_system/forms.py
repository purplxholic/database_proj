from django import forms

class AddMusicForm(forms.Form): 
    sid = forms.CharField(required=True)
    aid = forms.CharField(required=True)
    gid = forms.CharField(required=True)
    name = forms.CharField(required=True)
    releaseDate = forms.CharField(required=True)
    numDownloads = forms.CharField(required=True)
    numLicense = forms.CharField(required=True)
