from django.shortcuts import render, redirect
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def social(request):
    return render(request, 'social.html')

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


