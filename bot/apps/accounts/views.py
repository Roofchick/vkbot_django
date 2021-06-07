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
		
	a.name = request.POST['name']
	a.mark = request.POST['mark']
	a.sleep = request.POST['sleep']
	a.status = request.POST['status']
	
	
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
	

	return HttpResponseRedirect( reverse('Accounts:settings', args=(a.id,)) )

def new_account(request):
	return render(request, 'accounts/new_account.html')


def create(request):
	
	login = request.POST['login']
	password = request.POST['password']
	
	a = requests.get(f'https://api.vk.com/oauth/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={login}&password={password}')
	try:
		token = a.json()['access_token']
	except:
		return render(request, 'accounts/new_account.html', {'error': True})
	
	a = requests.get('https://api.vk.com/method/account.getProfileInfo', params={'v': 5.121, 'access_token': token})
	
	name = a.json()['response']['first_name']
	last_name = a.json()['response']['last_name']
		
	a = Account(call=f'{name} {last_name}', token=token)
	
	a.save()
	
	return render(request, 'accounts/settings.html', {'account': a})


def start(request):
	
	a = Status.objects.all()[0]
	a.work = True
	a.save()
	
	start_bot()
	
	accounts_list = Account.objects.all()
	
	return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})
	
	
def end(request):
	
	a = Status.objects.all()[0]
	a.work = False
	a.save()
	
	accounts_list = Account.objects.all()
	
	return render(request, 'accounts/list.html', {'accounts_list': accounts_list, 'start': a.work})