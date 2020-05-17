from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class ItemType(models.Model):

	name = models.CharField(max_length=50)
	detail = models.CharField(max_length=255, blank=True)
	default_width_x = models.PositiveSmallIntegerField()
	default_width_y = models.PositiveSmallIntegerField()
	default_is_openshut = models.BooleanField()
	default_is_mp = models.BooleanField()
	default_is_sequence = models.BooleanField()
	default_is_editable = models.BooleanField()

	def __str__(self):
		return self.name
