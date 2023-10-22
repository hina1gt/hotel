from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel')
router.register('room', RoomViewSet, basename='room')
router.register('booking', BookingViewSet, basename='booking')
router.register('guest', GuestViewSet, basename='guset')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls