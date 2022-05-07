from django.urls import path
from . import views


urlpatterns = [
    path('', views.ConferenceBookingListAPIView.as_view()),
    path('create/', views.ConferenceBookingCreateAPIView.as_view()),
    path('detail/<int:pk>/', views.ConferenceBookingDetailUpdateDeleteAPIView.as_view()),
]