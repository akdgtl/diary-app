from django.conf.urls import url
from . import views

app_name = 'daily'

urlpatterns = [
    url('', views.index,name='index'),
    url(r'^add/$', views.add,name='add'),
]
