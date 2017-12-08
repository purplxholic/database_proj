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
        query = "SELECT Songs.name as song_name, Artists.name as artist_name, Genres.name as genre_name, Songs.releaseDate from Songs INNER JOIN Artists INNER JOIN Genres"
        conditions = " WHERE Songs.aid = Artists.aid AND Songs.gid = Genres.gid"
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

        with connection.cursor() as cursor:
            cursor.execute(query + conditions)
            songs = dictfetchall(cursor, fetchall = True)
            
        #     for feedback in feedbacks: # iterate through feedbacks for a particular song to get ratings
        #         fuid = feedback['uid'] # the person who made the feedback
        #         cursor.execute("SELECT AVG(score) FROM Ratings GROUP BY fuid,sid HAVING fuid = %s AND sid = %s", [fuid, pk])
        #         r = cursor.fetchone()
        #         if r:
        #             feedback['rating'] = '{:.1f}'.format(r[0])
        #         else:
        #             feedback['rating'] = 0.0
        
        return songs

