from django.db import models

class item(models.Model):
    name=models.CharField(max_length=40)
    desc=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.CharField(max_length=600,default="https://st.depositphotos.com/1106005/3146/i/450/depositphotos_31468817-stock-photo-coming-soon-sign.jpg")

    def __str__(self):
        return self.name
