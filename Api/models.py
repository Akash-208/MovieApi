from django.db import models
from django.contrib.postgres.fields import ArrayField   #ArrayField can only be used when we are using postgreSQL

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=60)
    release_year = models.IntegerField(null=False,blank=False)
    rating = models.IntegerField(null=False,blank=False)
    geners = ArrayField(base_field=models.CharField(max_length=150),null=False,blank=False)
    actors = ArrayField(base_field=models.CharField(max_length=150),null=False,blank=False)

    def __str__(self):
        return self.name