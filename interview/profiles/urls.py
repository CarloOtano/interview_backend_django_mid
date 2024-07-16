
from django.urls import path
from interview.profiles.views import PlaceHolderView


urlpatterns = [
    path('', PlaceHolderView.as_view(), name='inventory-list'),
]