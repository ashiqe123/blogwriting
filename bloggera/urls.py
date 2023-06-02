from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view',views.view,name='view'),
    path('post2',views.post2,name='post2'),
    path('post3',views.post3,name='post3'),

]