from django.urls import path
from .views import function1, function2 ,function3

urlpatterns = [
    path('func1/', function1),
    path('func2/', function2),
    path('func3/', function3),
]