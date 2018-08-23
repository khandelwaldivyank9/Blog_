from . import views
from django.conf.urls import url
from django.contrib.auth import login,log
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$',logout, name='logout'),
    url(r'^create/$',views.createblog,name='create'),
    url(r'^view/$',views.viewblog,name='view'),
    url(r'update/(?P<pk>\d+)/$',views.updateblog,name='update'),
    url(r'delete/(?P<pk>\d+)/$',views.deleteblog,name='delete'),
]
