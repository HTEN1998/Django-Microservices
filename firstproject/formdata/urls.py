from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('basedetails',views.basedetails,name="basedetails"),
    path('login',views.login,name="login"),

    path('test_view',views.test_view,name='test')
]