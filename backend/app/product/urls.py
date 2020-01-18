from django.urls import path, include
# from .views import FlowerView, BunchView

# app_name = "flowers"

# app_name will help us do a reverse look-up latter.
# urlpatterns = [
#     path('', FlowerView.as_view()),
#     path('<int:pk>/', FlowerView.as_view()),
# ]

from rest_framework import routers
from .views import FlowerViewSet, BunchViewSet


api_router = routers.DefaultRouter()
api_router.register(r'flowers', FlowerViewSet)
api_router.register(r'bunches', BunchViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
]
