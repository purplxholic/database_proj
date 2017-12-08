from django import forms

class statisticsForm(forms.Form):
    howhigh = forms.CharField(required=True,min_length=0,label="Choose your Top No.")
    #left side is not displayed
    type_ofstats = [('song','By songs'),('artist','By Artists'),('genre','By genre'),('all','All')]
    stats = forms.ChoiceField(choices=type_ofstats,label="Sort by")
