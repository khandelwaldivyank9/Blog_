from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^create/$',views.createblog,name='create'),
    url(r'^view/$',views.viewblog,name='view'),
    url(r'update/(?P<pk>\d+)/$',views.updateblog,name='update'),
    url(r'delete/(?P<pk>\d+)/$',views.deleteblog,name='delete'),
]
