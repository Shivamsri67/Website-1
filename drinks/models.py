from django.db import models
class refre(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.CharField(max_length=1000)


    def __str__(self):
        return self.name

