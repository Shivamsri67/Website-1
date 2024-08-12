from django import forms
from .models import item
class itemform(forms.ModelForm):
    # name=forms.CharField(max_length=40)
    # desc=forms.CharField(max_length=30)
    # price=forms.IntegerField()
    # image=forms.CharField(max_length=600)
    class Meta:
        model=item
        fields='__all__'

    # def save(self,**cleaned_data):
    #     name=cleaned_data.get('name')
    #     desc=cleaned_data.get('desc')
    #     price=cleaned_data.get('price')
    #     image=cleaned_data.get('image')
    #     return item.objects.create(name=name,desc=desc,price=price,image=image)




    # def update(self,instance,**cleaned_data):    
    #     instance.name=cleaned_data.get('name',instance.name)
    #     instance.desc=cleaned_data.get('desc',instance.desc)
    #     instance.price=cleaned_data.get('price',instance.price)
    #     instance.image=cleaned_data.get('image',instance.image)
    #     instance.save()
    #     return instance



    