from django.urls import path
from index_page import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]