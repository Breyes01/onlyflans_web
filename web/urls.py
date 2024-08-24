from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_web'),
    path('about/', views.about, name='about_web'),
    path('welcome/', views.welcome, name='welcome_web'),
    path('contact/', views.contact, name='contact_web'),
    path('list_contact/', views.list_contact, name='list_contact_web'),
    path('delivery/', views.delivery, name='delivery_web')
]