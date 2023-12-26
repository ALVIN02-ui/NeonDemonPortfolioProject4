from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('reviewform/', views.reviewform, name = 'reviewform'),
    path('aaron/', views.aaron, name = 'aaron'),
    path('brandon/', views.brandon, name = 'brandon'),
    path('danny/', views.danny, name = 'danny'),
    path('leo/', views.leo, name = 'leo'),
]

#404 page handler
handler404 = 'NeonDemonSocialApp.views.styled_404'