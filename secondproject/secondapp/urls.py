from django.urls import path
from . import views

urlpatterns = [
    path('userdetails',views.getuserdetails,name = 'micro1')
]