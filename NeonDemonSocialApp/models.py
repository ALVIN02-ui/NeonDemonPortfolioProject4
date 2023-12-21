from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class UploadImage(models.Model):
    """
    Class containing the model for uploading an image
    """

    Uploaded_image = CloudinaryField('image', default='placeholder')
    alt = models.TextField(max_length=50)
    date_uploaded = models.DateField(auto_now_add=True)   
    
    class Meta:
        ordering = ['-date_uploaded']



class Review(models.Model):
    """
    Class containing the model for leaving a review on the page.
    """
    rating = models.IntegerField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.content} review left by: {self.name}"
