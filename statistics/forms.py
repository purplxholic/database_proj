from django import forms

class statisticsForm(forms.Form):
    howhigh = forms.CharField(required=True,min_length=0,label="Choose your Top No.")
    #left side is not displayed
    type_ofstats = [('song','By songs'),('artist','By Artists'),('genre','By genre'),('all','All')]
    months = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),('all','All Months')]
    stats = forms.ChoiceField(choices=type_ofstats,label="Sort by")
    month = forms.ChoiceField(choices=months,label="Month")
