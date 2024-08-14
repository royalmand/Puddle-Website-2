from django.urls import path
from . import views 

# ini dipake untuk call url di base html
app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]