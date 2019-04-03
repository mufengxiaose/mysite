from django.urls import path
from news import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive)
]