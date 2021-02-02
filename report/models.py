from django.db import models

class Report(models.Model):
    ward_name= models.CharField(max_length=100)
    population= models.IntegerField()
    water_supply= models.IntegerField()
    content= models.TextField()

    def __str__(self):
        return self.ward_name
