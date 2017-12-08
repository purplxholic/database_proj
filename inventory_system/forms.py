from django import forms

class AddMusicForm(forms.Form):
    sid = forms.CharField(required=True,max_length=10,min_length=10,
                        label="Song ID")
    aid = forms.CharField(required=True,max_length=10,min_length=10,label="Artist ID")
    gid = forms.CharField(required=True,max_length=10,min_length=10,label="Genre ID")
    name = forms.CharField(required=True,max_length=50,min_length=0,help_text='Max 50 Char',label="Song Name")
    releaseDate = forms.CharField(required=True,label="Release Date",help_text='Format: YYYY-MM-DD')
    numDownloads = forms.CharField(required=True,label="No. of Downloads",help_text='For new songs, it should be 0')
    numLicense = forms.CharField(required=True,label="No. of License")

class licenseForm(forms.Form):
    sid = forms.CharField(required=True,max_length=10,min_length=10,
                        label="Song ID")
    amt = forms.CharField(required=True,
                        label="New no. of licenses")
