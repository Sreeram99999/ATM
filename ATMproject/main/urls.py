from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home,name='home'),
    path('validate_pin',views.validate_pin,name='validate_pin'),
    path('with <int:pk>',views.withdraw,name="with"),
    path('deposite <int:pk>',views.deposite,name='deposite'),
    path('transfer <int:pk>',views.transfer,name='transfer'),
    path('forget',views.forgetpin,name='forget'),
    path('check/<int:c>/<int:i>',views.check,name='check'),
    path('re <int:pk>',views.re_enter,name='re'),
    path('history <int:pk>',views.history,name='history'),
    path('about',views.about,name='about'),
    path('service',views.ser,name='service'),
    path('contact',views.con,name='contact'),

]