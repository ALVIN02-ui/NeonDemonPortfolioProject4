from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponseRedirect, Http404
from .forms import ReviewForm, UploadImageForm
from .models import Review, UploadImage
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def styled_404(request, exception):
    # View for the 404.html page
    return render(request, '404.html', {}, status = 404)


def base(request):
    #View for the base.html page
    return render(request, 'base.html')


def index(request):
    # View for the index.html page
    return render(request, 'index.html')


def about(request):
    # View for the about.html page
    uploaded_images = UploadImage.objects.all()
    return render(request, 'about.html', {'uploaded_images': uploaded_images})


def gallery(request):
    """
    Displays the gallery.html file,
    gets the superuser from django, 
    checks who has uploaded the image,
    gives option to delete the photo if uploader is logged in
    """
    superusers = User.objects.filter(is_superuser = True)
    superuser_usernames = list(superusers.values_list('username', flat = True))

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'delete':
                image_id = request.POST['image_id']
                image_to_delete = get_object_or_404(UploadImage, id=image_id)
                if image_to_delete.uploaded_by == request.user:
                    image_to_delete.delete()
                    messages.success(request, 'Image deleted successfully.')
                else:
                    messages.error(request, 'You are not allowed to delete this image.')
            elif action == 'edit':
                image_id = request.POST['image_id']
                image_to_edit = get_object_or_404(UploadImage, id=image_id)
                if image_to_edit.uploaded_by == request.user:
                    new_alt_text = request.POST.get('alt_text', '')
                    image_to_edit.alt = new_alt_text
                    image_to_edit.save()
                    messages.success(request, 'Image updated successfully.')
                else:
                    messages.error(request, 'You cannot edit this image')

        # Handle image upload if the request is for image upload
        elif form.is_valid():
            new_image = form.save(commit = False)
            new_image.uploaded_by = request.user
            new_image.save()
            messages.success(request, 'Image uploaded successfully.')
            return HttpResponseRedirect(reverse('gallery'))
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

@login_required
def reviewform(request):
    """
    Ensures a user is logged in before submitting the form,
    gets the logged in user from django, 
    Saves the form.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  
            review.user = request.user  
            review.save()  
            return HttpResponseRedirect('/reviews/')
    else:
        form = ReviewForm()

    return render(request, 'reviewform.html', {'form': form})



def reviews(request):
    reviews = Review.objects.select_related('user').all()
    
    context = {
        'reviews': reviews,
    }
    
    return render(request, 'reviews.html', context)


def my_review(request):
    if request.method == 'POST' and 'action' in request.POST:
        action = request.POST.get('action')
        if action == 'delete':
            review_id = request.POST.get('review_id')
            review_to_delete = get_object_or_404(Review, id=review_id)
            if review_to_delete.user == request.user:
                review_to_delete.delete()
                messages.success(request, 'Review deleted successfully.')
            else:
                messages.error(request, 'You are not allowed to delete this review.')
            return redirect('/myreview/')
        
        elif action == 'edit':
            review_id = request.POST.get('review_id')
            review_to_edit = get_object_or_404(Review, id=review_id)
            if review_to_edit.user == request.user:
                new_rating = request.POST.get('review_rating')
                new_content = request.POST.get('review_content', '')
                if new_rating and new_rating.isdigit():
                    new_rating = int(new_rating)
                    if 1 <= new_rating <= 5:
                        review_to_edit.rating = new_rating
                        review_to_edit.content = new_content  # Correct assignment
                        review_to_edit.save()
                        messages.success(request, 'Review updated successfully.')
                    else:
                        messages.error(request, 'Rating must be between 1 and 5.')
                else:
                    messages.error(request, 'Invalid rating value.')
            else:
                messages.error(request, 'You cannot edit this review')
    else:
        messages.error(request, 'Invalid request')

    reviews = Review.objects.filter(user=request.user).select_related('user')
    context = {
        'reviews': reviews,
    }
    return render(request, 'myreview.html', context)



def aaron(request):
    """
    view for aaron.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    specific_user = User.objects.get(username = 'neondemonaaron')
    user_id = specific_user.id
    uploaded_images = UploadImage.objects.filter(uploaded_by = user_id)
    return render(request, 'aaron.html', {'uploaded_images': uploaded_images})


def brandon(request):
    """
    view for brandon.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    specific_user = User.objects.get(username = 'neondemonbran')
    user_id = specific_user.id
    uploaded_images = UploadImage.objects.filter(uploaded_by = user_id)
    return render(request, 'brandon.html', {'uploaded_images': uploaded_images})


def danny(request):
    """
    view for danny.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    specific_user = User.objects.get(username = 'neondemondan')
    user_id = specific_user.id
    uploaded_images = UploadImage.objects.filter(uploaded_by = user_id)
    return render(request, 'danny.html', {'uploaded_images': uploaded_images})


def leo(request):
    """
    view for leo.html page, gets the user id and pushes their photos they
    uploaded into individual galleries.
    """
    specific_user = User.objects.get(username = 'neondemonleo')
    user_id = specific_user.id
    uploaded_images = UploadImage.objects.filter(uploaded_by = user_id)
    return render(request, 'leo.html', {'uploaded_images': uploaded_images})




