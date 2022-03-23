import threading

from main import main

from accounts.models import Account


def start_bot():
	
	for a in Account.objects.all():
		
		ac = a.id
		TOKEN = a.token
		STATUS = a.status
		SLEEP = a.sleep
		MARK = a.mark
		NAME = a.name
		auto_friends = a.auto_friends
		ls_user = a.ls_user
		group_name = a.group_name
		base_name = a.base_name
		group = a.group
		commands = a.commands
		voice_bot = a.voice_bot
		reply = a.reply
		
		
		try:
			threading.Thread(target=main, args=(ac, TOKEN, STATUS, SLEEP, MARK, NAME, auto_friends, ls_user, group_name, base_name, group, commands, voice_bot, reply)).start()
		except Exception as err:
			print(err)