from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('handlelogin', views.handlelogin,name="handlelogin"),
    path('handlelogout', views.handlelogout,name="handlelogout"),
    path('signup', views.signup,name="signup"),
    path('handlesignup', views.handlesignup,name="handlesignup"),
    path('utilshome',views.utilshome,name="utilshome"),
    path('analyze',views.analyze,name="analyze"),
]
