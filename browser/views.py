from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .forms import BrowseForm

from music_store.utils import dictfetchall

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
    template_name = "browse_results.html"

    def get_context_data(self, **kwargs):
        context = super(BrowseResultsView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = "SELECT Songs.name as song_name, Artists.name as artist_name, Genres.name as genre_name, Songs.releaseDate, Score.avg_score from Songs INNER JOIN Artists INNER JOIN Genres INNER JOIN (SELECT AVG(score) as avg_score, sid FROM Feedbacks GROUP BY uid,sid) as Score"
        conditions = " WHERE Songs.aid = Artists.aid AND Songs.gid = Genres.gid AND Score.sid = Songs.sid" 
        name = self.request.GET.get('Name') 
        if (name is not ""):
            conditions += " AND Songs.name LIKE '%%" + name + "%%'"

        artist = self.request.GET.get('Artist')
        if (artist is not ""):
            if (conditions is not ""):
                conditions += " AND Artists.name LIKE '%%" + artist + "%%'"
                
        genre = self.request.GET.get('Genre')
        if (genre is not ""):
            if (conditions is not ""):
                conditions += " AND Genres.name LIKE '%%" + genre + "%%'"
            
        sort = " ORDER BY avg_score DESC"

        with connection.cursor() as cursor:
            cursor.execute(query + conditions + sort)
            songs = dictfetchall(cursor, fetchall = True)
            
        return songs

