from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('new_account', views.new_account, name = 'new_account'),
	path('<int:account_id>/', views.settings, name = 'settings'),
	path('<int:account_id>/save', views.save, name = 'save'),
	path('create', views.create, name = 'create'),
	path('start', views.start, name='start'),
	path('end', views.end, name='end'),
]