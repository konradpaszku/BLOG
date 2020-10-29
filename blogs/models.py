from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """WPIS NA BLOGU"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Zwraca model w postaci stringa"""
        return self.text