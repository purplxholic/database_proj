from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from inventory_system.models import Song

from .forms import BrowseForm

from feedback_rating.utils import dictfetchall

class BrowseView(FormView):
    template_name = "index.html"
    form_class = BrowseForm
    fields = ['Artist', 'Name', 'Genre']
    success_url = 'results'

    def get_context_data(self, **kwargs):
        context = super(BrowseView, self).get_context_data(**kwargs)
        context['fields'] = self.fields

        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_query()
        return super(BrowseView, self).form_valid(form)

class BrowseResultsView(ListView):
    model = Song
    template_name = "browse_results.html"

    def get_context_data(self, **kwargs):
        context = super(BrowseResultsView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = "SELECT * from inventory_system_song"
        conditions = ""
        name = self.request.GET.get('Name') 
        if (name is not ""):
            conditions += " WHERE name LIKE '%%" + name + "%%'"

        artist = self.request.GET.get('Artist')
        if (artist is not ""):
            query += ", inventory_system_artist"
            if (conditions is not ""):
                conditions += " AND inventory_system_artist.name LIKE '%%" + artist + "%%'"
            else:
                conditions += " WHERE inventory_system_artist.name LIKE '%%" + artist + "%%'"
                
        genre = self.request.GET.get('Genre')
        if (genre is not ""):
            query += ", inventory_system_genre"
            if (conditions is not ""):
                conditions += " AND inventory_system_genre.name LIKE '%%" + genre + "%%'"
            else:
                conditions += " WHERE inventory_system_genre.name LIKE '%%" + genre + "%%'"

        return Song.objects.raw(query + conditions)
