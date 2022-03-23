from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from .models import Account, Status

import requests

from func.account_start import start_bot

a = Status.objects.all()[0]
if a.work:
	start_bot()

def index(request):
	a = Status.objects.all()[0]
	accounts_list = Account.objects.all()
	return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})

def settings(request, account_id):
	try:
		a = Account.objects.get( id = account_id )
	except:
		raise Http404('Аккаунт не найден')

	return render(request, 'accounts/settings.html', {'account': a})


def save(request, account_id):
	try:
		a = Account.objects.get( id = account_id )
	except:
		raise Http404('Аккаунт не найден')
		
	try:
		a.name = request.POST['name']
	except:
		pass

	try:
		a.mark = request.POST['mark']
	except:
		pass
	
	try:
		a.sleep = request.POST['sleep']
	except:
		pass

	try:
		a.status = request.POST['status']
	except:
		pass
	
	try:
		x = request.POST['auto_friends']
		a.auto_friends = True
	except:
		a.auto_friends = False
	
	try:
		x = request.POST['ls_user']
		a.ls_user = True
	except:
		a.ls_user = False
	
	try:
		x = request.POST['group_name']
		a.group_name = True
	except:
		a.group_name = False
	
	try:
		x = request.POST['voice_bot']
		a.voice_bot = True
	except:
		a.voice_bot = False
	
	try:
		x = request.POST['reply']
		a.reply = True
	except:
		a.reply = False
		
		

	a.save()

	base_name = request.POST['base_name']
	try:
		with open(f"base/{base_name}") as f:
			pass
		a.base_name = base_name
		a.save()
		return HttpResponseRedirect( reverse('Accounts:settings', args=(a.id,)) )
	except:
		print(base_name)
		return render(request, 'accounts/settings.html', {'account': a, 'error_base': base_name})
	

def new_account(request):
	return render(request, 'accounts/new_account.html')

def new_account_token(request):
	return render(request, 'accounts/new_account_token.html')

def new(request):
	return render(request, 'accounts/new.html')

def new_acc_login_or_token(request):
	return render(request, 'accounts/new_acc_login_or_token.html')
	
def create_group(request):
	
	token = request.POST['longpoll_token']
	
	id = request.POST['id']
	
	a = requests.get('https://api.vk.com/method/groups.getLongPollServer', params={'lp_version': 3, 'v': 5.121 , 'access_token': token, 'group_id': id})
	
	try:
		ts = a.json()['response']['ts']
	except:
		return render(request, 'accounts/new_account.html', {'error': True})
		
	a = requests.get('https://api.vk.com/method/groups.getById', params={'access_token': token, 'group_id': id, 'v': 5.121})
	
	name = a.json()['response'][0]['name']
		
	a = Account(call=name, token=token, group=id)
	
	a.save()
	
	return render(request, 'accounts/settings.html', {'account': a})
	
def new_group(request):
	return render(request, 'accounts/new_group.html')

def create_account(request):
	
	login = request.POST['login']
	password = request.POST['password']
	
	a = requests.get(f'https://api.vk.com/oauth/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={login}&password={password}')
	try:
		token = a.json()['access_token']
	except:
		print(a.text)
		return render(request, 'accounts/new_account.html', {'error': True})
	
	a = requests.get('https://api.vk.com/method/account.getProfileInfo', params={'v': 5.121, 'access_token': token})
	
	name = a.json()['response']['first_name']
	last_name = a.json()['response']['last_name']
		
	a = Account(call=f'{name} {last_name}', token=token)
	
	a.save()
	
	return render(request, 'accounts/settings.html', {'account': a})


def start(request):
	
	a = Status.objects.all()[0]

	accounts_list = Account.objects.all()

	if accounts_list:
		
		a.work = True
		a.save()
		
		start_bot()
	
		return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})

	else:
		return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})
	
	
def end(request):
	
	a = Status.objects.all()[0]
	a.work = False
	a.save()
	
	accounts_list = Account.objects.all()
	
	return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})
	
def delete_yesno(request, account_id):
	return render(request, 'accounts/delete_yesno.html', {'account_id': account_id})
	
def delete_account(request, account_id):
	Account.objects.get(id=account_id).delete()
	return index(request)

def create_account_token(request):
	
	token = request.POST['token']
	
	a = requests.get('https://api.vk.com/method/account.getProfileInfo', params={'v': 5.121, 'access_token': token})

	try:
		name = a.json()['response']['first_name']
		last_name = a.json()['response']['last_name']
	except:
		return render(request, 'accounts/new_account_token.html', {'error': True})
	
	a = requests.get('https://api.vk.com/method/account.getProfileInfo', params={'v': 5.121, 'access_token': token})
		
	a = Account(call=f'{name} {last_name}', token=token)
	
	a.save()
	
	return render(request, 'accounts/settings.html', {'account': a})