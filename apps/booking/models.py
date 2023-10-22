from django.db.models import *

from apps.room.models import *
from apps.guest.models import *

class Booking(Model):

    room = ForeignKey(Room, on_delete=CASCADE)
    guest  = ForeignKey(Guest, on_delete=CASCADE)
    check_in_date = DateField(auto_now_add=True)
    check_out_date = DateField(blank=True, null=True)
    is_paid = BooleanField(default=False)

    def __str__(self):
        return f'{self.room} by {self.guest}'