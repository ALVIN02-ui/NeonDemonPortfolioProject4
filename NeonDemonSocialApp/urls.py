from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('social/', views.social, name='social'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviewform/', views.reviewform, name='reviewform'),
    handler404 = TemplateView.as_view(template_name='404.html')
]