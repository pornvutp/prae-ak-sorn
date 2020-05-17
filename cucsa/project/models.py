from django.db import models
from django.contrib.auth import get_user_model
from infrastructure.models import ItemType

# Create your models here.
User = get_user_model()

class Project(models.Model):

	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	detail = models.CharField(max_length=255, blank=True)
	num_seat_x = models.PositiveSmallIntegerField()
	num_seat_y = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name

class Announcement(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	publisher = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, blank=True)
	detail = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.title

class Dimension(models.Model):

	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	ItemType = models.ForeignKey(ItemType, on_delete=models.CASCADE)
	default_width_x = models.PositiveSmallIntegerField()
	width_y = models.PositiveSmallIntegerField()
	is_openshut = models.BooleanField()
	is_mp = models.BooleanField()
	is_sequence = models.BooleanField()
	is_editable = models.BooleanField()

	def __str__(self):
		return self.title + '_' + self.ItemType
