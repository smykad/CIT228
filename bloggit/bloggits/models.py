from django.db import models

# Create your models here.
class Bloggit(models.Model):
    """A blog entry."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Bloggit, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
