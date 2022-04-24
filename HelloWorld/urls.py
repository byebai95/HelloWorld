from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, path, include

from . import views, search

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    re_path(r'^hello/$', views.hello),
    re_path(r'^runoob/$', views.runoob),
    re_path(r'^script/$', views.script),
    re_path(r'^iftest/$', views.iftest),
    re_path(r'^fortest/$', views.fortest),
    re_path(r'^href/$', views.href),

    re_path(r'^search-form/$', search.search_form),
    re_path(r'^search/$', search.search),

    path('model/', include('TestModel.urls')),

    path('env/', views.envtest),

]
