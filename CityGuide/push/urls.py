from django.conf.urls import url

from . import views

app_name = 'push'

urlpatterns = [
	url(r'^$' , views.index , name = 'index') ,
]