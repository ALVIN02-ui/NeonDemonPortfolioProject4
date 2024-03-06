from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


# Create your models here.

class UploadImage(models.Model):
    """
    Class containing the model for uploading an image
    """
    uploaded_by = models.ForeignKey(get_user_model(),
                                    on_delete=models.CASCADE, null=True,
                                    blank=True)
    Uploaded_image = CloudinaryField('image', blank=True)
    alt = models.TextField(max_length=50)
    date_uploaded = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_uploaded']

    class Meta:
        ordering = ['-date_uploaded']


class Review(models.Model):
    """
    Class containing the model for leaving a review on the page.
    """
    rating = models.IntegerField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.content} review left by: {self.user}"
