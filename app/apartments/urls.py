from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apartments"),
    path('<int:apartment_id>/', views.apartment, name="apartment"),
    path('search', views.search, name="search"),
    path('favorits', views.favorits, name="favorits"),
]
