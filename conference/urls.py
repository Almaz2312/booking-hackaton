from django.urls import path
from . import views


urlpatterns = [
    path('', views.ConferenceListAPIView.as_view()),
    path('detail/<int:pk>/', views.ConferenceDetailAPIView.as_view()),
]
