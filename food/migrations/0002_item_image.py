# Generated by Django 4.2 on 2024-07-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://st.depositphotos.com/1106005/3146/i/450/depositphotos_31468817-stock-photo-coming-soon-sign.jpg', max_length=600),
        ),
    ]
