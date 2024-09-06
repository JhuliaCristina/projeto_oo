from django.urls import path
from vesper import views

urlpatterns = [
    path('', views.index , name =  'index' ),
]
