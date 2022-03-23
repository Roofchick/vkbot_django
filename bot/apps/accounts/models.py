from django.db import models


class Account(models.Model):
	call = models.CharField('Имя бота', max_length=30)
	token = models.CharField('Токен бота', max_length=100)
	name = models.CharField('Обращение бота', max_length=15, default='Бот')
	sleep = models.PositiveIntegerField('Задержка перед отправкой сообщения', default=0)
	voice_bot = models.BooleanField('Ответ голосовыми сообщениями', default=False)
	status = models.TextField('Статус', default='vk.com/roofchick')
	mark = models.CharField('Метка бота', max_length=15, default='bot')
	auto_friends = models.BooleanField('Автоматическое добавление в друзья', default=True)
	ls_user = models.BooleanField('Обращение в личных сообщениях', default=True)
	group_name = models.BooleanField('Обращение к пользователю в беседах', default=False)
	base_name = models.CharField('База ответов', max_length=15, default='base.bin')
	group = models.PositiveIntegerField('id сообщества, у пользователей = 0', default=0)
	commands = models.TextField('Команды (не работает)', default='.')
	reply = models.BooleanField('Пересылать сообщения собеседника в беседах', default=True)
	

class Status(models.Model):
	
	name = models.TextField('Э', default='Ы')
	
	work = models.BooleanField('Статус работы аккаунтов', default=False)
	
	
	def __str__(self):
		return self.name