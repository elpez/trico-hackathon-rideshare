from django.conf.urls import url

from . import views

app_name = 'ridematch'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mode>finder|sharer)/$', views.finder_sharer, name='finder_sharer'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
