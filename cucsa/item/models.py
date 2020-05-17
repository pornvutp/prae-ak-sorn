from django.db import models
from project.models import Project, ItemTag, TypeDimension

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Item(models.Model):

	name = models.CharField(max_length=50)
	detail = models.TextField(max_length=500)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	type_dimension = models.ForeignKey(TypeDimension, on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField()

	tag = models.ForeignKey(ItemTag, on_delete=models.SET_DEFAULT, default='')

	def __str__(self):
		return self.project + '-' + self.name

class ItemDraft(models.Model):

	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField()

	detail = models.TextField(max_length=500)

	def __str__(self):
		return self.project + '-' + self.name

class Review(models.Model):

	draft = models.ForeignKey(ItemDraft, on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)

	comment = models.TextField(max_length=500)
