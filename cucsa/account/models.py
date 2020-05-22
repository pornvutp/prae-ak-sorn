from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.


class UserProfileInfo(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	short_bio = models.CharField(max_length=255, blank=True)
	profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

	def __str__(self):
		return self.user.username
