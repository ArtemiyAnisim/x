from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact,
         {'phone': '+79872348074', 'social_network': 'https://vk.com/id524023405',
          'address': 'Окружное шоссе 28', 'link': 'https://github.com/ArtemiyAnisim'}, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('form/', views.form),
]