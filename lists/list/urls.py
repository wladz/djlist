from django.urls import path

from list.views import index

urlpatterns = [
    path('', index, name='home'),
]