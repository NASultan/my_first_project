from django.urls import path
from . import views
urlpatterns = [
	path('', views.main, name='main'),
	path('main', views.main, name='main'),
	path('news', views.news, name='news'),
	path('clean', views.clean, name='clean'),
	path('services', views.services, name='services'),
	path('outsourcing', views.outsourcing, name='outsourcing'),
	path('repairs_laptop', views.repairs_laptop, name='repairs_laptop'),
	path('repairs', views.repairs, name='repairs'),
	path('recovery', views.recovery, name='recovery'),
	path('assembly', views.assembly, name='assembly'),
	path('price', views.price, name='price'),
	path('contacts', views.contacts, name='contacts'),
]
