from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    file = models.FileField(upload_to="uploads/music/")
