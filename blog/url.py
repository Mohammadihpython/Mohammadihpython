from django.urls import  path
from . import views
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('', views.Home, name ='home'),
]
