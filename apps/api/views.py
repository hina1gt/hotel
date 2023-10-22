from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from apps.guest.models import *
from apps.hotel.models import *
from apps.booking.models import *
from apps.room.models import *

class HotelViewSet(ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomViewSet(ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookingViewSet(ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    
