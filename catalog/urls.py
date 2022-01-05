from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cars/', views.CarsListView.as_view(), name='cars'),
    path('car/<str:pk>', views.CarsDetailView.as_view(), name='car-detail'),
    path('pilots/', views.PilotListView.as_view(), name='pilots'),
    path('pilots/<str:pk>', views.PilotsDetailView.as_view(), name='pilot-detail'),
]