from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponseRedirect, Http404
from .forms import ReviewForm
from .models import Review

# Create your views here.

def styled_404(request, exception):
    return render(request, '404.html', {}, status=404)

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    #gets the superuser variable
    superusers = User.objects.filter(is_superuser=True)
    superuser_usernames = list(superusers.values_list('username', flat=True))
    return render(request, 'gallery.html', {'superuser_usernames': superuser_usernames})
    

def reviewform(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            validators=[
            MinValueValidator(1, message='Rating should be at least 1'),
            MaxValueValidator(5, message='Rating should not exceed 5')
        ]
            form.save()
            return HttpResponseRedirect('/reviews/')
    else:
        form = ReviewForm()

    return render(request, 'reviewform.html', {'form': form})
    
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


