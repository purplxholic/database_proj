from django import forms

class BrowseForm(forms.Form):
    Name = forms.CharField(required=False)
    Artist = forms.CharField(required=False)
    Genre = forms.CharField(required=False)

    def send_query(self):
        # send query
        pass