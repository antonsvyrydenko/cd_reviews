from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from news.models import Article

value='true'

urlpatterns = [
	url(r'^about/$', views.info, name='info'),
	url(r'^$', ListView.as_view(queryset=Article.objects.all().order_by("-date")[:1], template_name="news/posts.html"), {'check':value}),
]
