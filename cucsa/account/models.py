from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	short_bio = models.CharField(max_length=255, blank=True)
	profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

	def __str__(self):
		return self.user.email
