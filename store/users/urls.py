from django.urls import path

from .views import CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]
