from django.conf import settings
from django.contrib.auth.hashers import check_password
from app_core.models import Administrador, Egresado, User, SuperUser

class AdminBackend:
	def authenticate(self, request, email=None, password=None):
		print("Hhere0")
		try:
			print(email)
			print(password)
			user = 	Administrador.objects.get(email=email, password=password)
			return user
		except Administrador.DoesNotExist:
			return None

	def get_user(self, user_id):
		print("gwt0")
		try:
			print(Administrador.objects.get(pk=user_id))
			return Administrador.objects.get(pk=user_id)
		except Administrador.DoesNotExist:
			return None

class EgresadoBackend:    
	def authenticate(self, request, email=None, password=None):
		print("Here3")
		print("Hhere1")
		print(password)
		try:
			user = 	Egresado.objects.get(email=email, password=password)
			return user
		except Egresado.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			print("get1")
			return Egresado.objects.get(pk=user_id)
		except Egresado.DoesNotExist:
			return None

class SuperUserBackend:   
	print("wwwww") 
	def authenticate(self, request, email=None, password=None):
		try:
			print("hi2")
			user = 	SuperUser.objects.get(email=email)
			success=user.check_password(password)
			if success:
				return user
			else:
				return None
		except SuperUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			print("get2")
			return SuperUser.objects.get(pk=user_id)
		except SuperUser.DoesNotExist:
			return None



