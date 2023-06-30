from django.urls import path
from .views import index, add_index

urlpatterns = [
    path('', index),
    path('add/', add_index),

]

