from django.urls import path
from .views import FlowerView
from django.conf.urls import url


app_name = "flowers"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('/', FlowerView.as_view()),
    path('/<int:pk>', FlowerView.as_view())
    # url(r'^', FlowerView.as_view()),
]
