from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^GetCountry/$',GetCountry,name="GetCountry"),
	url(r'^Contact/$',Contact,name="Contact"),
	url(r'^Details_Property/(\d+)/$',Details_Property,name="Details_Property"),
]