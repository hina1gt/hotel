from django.db.models import *

class Guest(Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()
    phone_number = CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name}'
    