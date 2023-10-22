from django.db.models import *

class Hotel(Model):

    name = CharField(max_length=256)
    address = CharField(max_length=256)
    city = CharField(max_length=256)
    country = CharField(max_length=256)
    rating = DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'{self.name}'

