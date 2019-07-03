from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),
    
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    
    #/music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    
    #/music/album_id/2/
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    
    #/music/album_id/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
       
]


