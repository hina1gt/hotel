from rest_framework.serializers import *

from apps.guest.models import *
from apps.hotel.models import *
from apps.booking.models import *
from apps.room.models import *

class GuestSerializer(ModelSerializer):

    class Meta:
        model = Guest
        fields = '__all__'

class HotelSerializer(ModelSerializer):

    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'