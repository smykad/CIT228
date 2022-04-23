"""Defines URL patterns for bloggits."""

from django.urls import path

from . import views

app_name = 'bloggits'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the bloggits
    path('bloggits/', views.bloggits, name='bloggits'),
    # Detail page for a single topic.
    path('bloggits/<int:bloggit_id>/', views.bloggit, name='bloggit'),

]