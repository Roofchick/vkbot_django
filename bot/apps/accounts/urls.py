from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('new_account', views.new_account, name = 'new_account'),
	path('new_account_token', views.new_account_token, name = 'new_account_token'),
	path('new_acc_login_or_token', views.new_acc_login_or_token, name='new_acc_login_or_token'),
	path('new', views.new, name='new'),
	path('new_group', views.new_group, name='new_group'),
	path('<int:account_id>/', views.settings, name = 'settings'),
	path('<int:account_id>/save', views.save, name = 'save'),
	path('create_account', views.create_account, name = 'create_account'),
	path('create_account_token', views.create_account_token, name = 'create_account_token'),
	path('create_group', views.create_group, name='create_group'),
	path('start', views.start, name='start'),
	path('end', views.end, name='end'),
	path('<int:account_id>/delete_yesno', views.delete_yesno, name='delete_yesno'),
	path('<int:account_id>/delete_account', views.delete_account, name='delete_account'),
]