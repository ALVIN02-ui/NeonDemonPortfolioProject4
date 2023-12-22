from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponseRedirect, Http404
from .forms import ReviewForm, UploadImageForm
from .models import Review, UploadImage

# Create your views here.

def styled_404(request, exception):
    # View for the 404.html page
    return render(request, '404.html', {}, status=404)


def base(request):
    #View for the base.html page
    return render(request, 'base.html')


def index(request):
    # View for the index.html page
    return render(request, 'index.html')


def about(request):
    # View for the about.html page
    return render(request, 'about.html')


def gallery(request):
    # View for the gallery.html page
    # Gets the superuser variable
    superusers = User.objects.filter(is_superuser=True)
    superuser_usernames = list(superusers.values_list('username', flat=True))
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.uploaded_by = request.user
            new_image.save()
            messages.success(request, 'Image uploaded successfully.')
        else:
            messages.error(request, 'Unable to upload your image')
    else:
        form = UploadImageForm()
    uploaded_images = UploadImage.objects.all()
    context = {
        'form': form,
        'superuser_usernames': superuser_usernames,
        'galleryImages': uploaded_images
        }
    return render(request, 'gallery.html', context)


def reviewform(request):
    # View for the reviewform.html page
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            validators = [
                MinValueValidator(1, message='Rating should be at least 1'),
                MaxValueValidator(5, message='Rating should not exceed 5')
            ]
            form.save()
            return HttpResponseRedirect('/reviews/')
    else:
        form = ReviewForm()

    return render(request, 'reviewform.html', {'form': form})


def reviews(request):
    # View for the reviews.html page
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


def aaron(request):
    """
    view for aaron.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    specific_user = User.objects.get(username='neondemonaaron')
    user_id = specific_user.id
    uploaded_images = UploadImage.objects.filter(uploaded_by=user_id)
    return render(request, 'aaron.html', {'uploaded_images': uploaded_images})


def brandon(request):
    """
    view for brandon.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    return render(request, 'brandon.html')


def danny(request):
    """
    view for danny.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    return render(request, 'danny.html')


def leo(request):
    """
    view for leo.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    return render(request, 'leo.html')
