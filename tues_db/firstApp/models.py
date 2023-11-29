from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class PersonIdCard(models.Model):
    number = models.TextField()

    def __str__(self):
        return '{}'.format(self.number)


class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    id_card = models.OneToOneField(PersonIdCard, on_delete=DO_NOTHING)
    email = models.TextField(null=True)

    def __str__(self):
        return '{},{},{}'.format(self.first_name, self.last_name, self.id_card)
