
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    doi_link = models.URLField()
    pdf_file = models.FileField(upload_to='pdfs/')

