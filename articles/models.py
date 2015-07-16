import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True,max_length=255)
	author = models.ForeignKey(User)
	published = models.BooleanField()
	pub_date = models.DateTimeField('date published')
	created_date = models.DateTimeField('created date')
	body = models.TextField()

	def __str__(self):
		return self.title

	def published(self):
		return self.published

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)