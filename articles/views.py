from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Article

class ArticleIndexView(generic.DetailView):
	model = Article
	template_name = 'articles/index.html'