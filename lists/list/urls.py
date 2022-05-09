from django.urls import path

from list.views import index, revers

urlpatterns = [
    path('', index, name='home'),
    path('revers/', revers, name='revers'),
]