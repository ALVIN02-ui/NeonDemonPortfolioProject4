from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class UploadImage(models.Model):
    """
    Class containing the model for uploading an image
    """
    
    Uploaded_image = CloudinaryField('image', default='placeholder')
    date_uploaded = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='photo_likes',blank=True)

    class Meta:
        ordering = ['-date_uploaded']

    def number_of_likes(self):
        """
        Returns the number of people who have liked an image
        """
        return self.likes.count()

class Review(models.Model):
    """
    Class containing the model for leaving a review on the page.
    """
    title = models.CharField(max_length=200, unique=True) 
    rating = models.IntegerField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.content} review left by: {self.name}"
