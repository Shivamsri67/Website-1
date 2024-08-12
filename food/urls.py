app_name='food'
from django.urls import path
from . import views
from django.urls import include
urlpatterns=[ path('index/',views.index,name="index"),
             path('detail/<int:pk>/',views.detail,name='detail'),
             path("",views.home,name="home"),
             path('insert',views.add_item,name="insert"),
             path('update/<int:pk>',views.edit_item,name='update'),
             path('delete/<int:pk>/',views.delete_item,name='delete'),
             
             ]