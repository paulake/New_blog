from django.conf.urls import url, include
from . import views
from django.urls import path 

urlpatterns = [
	url(r'^$', views.home_view, name='home_view'),
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/category/(?P<category_name>)/$', views.post_list, name='categorised_list'),
    path('post/category/<category_name>/', views.post_list, name='categorised_list'),
    

]


