# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Need to add constraints

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    num_downloads = models.IntegerField()
    num_license = models.IntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, related_name="purchases", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "song"),)

    def __str__(self):
        return (self.user, self.song)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="feedbacks", on_delete=models.CASCADE)
    score = models.IntegerField()
    post_date = models.DateField()
    comments = models.CharField(max_length=250)
   
    class Meta:
        unique_together = (("user", "song"),) 

    def __str__(self):
        return (self.user, self.song)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE) 
    feedback = models.ForeignKey(Feedback, related_name="ratings", on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = (("user", "song", "feedback"),) 

    def __str__(self):
        return (self.user, self.song, self.feedback)
