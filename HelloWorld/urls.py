from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views, search

urlpatterns = [

    # url(r'^admin/$', admin.site.urls),

    url(r'^hello/$', views.hello),
    url(r'^runoob/$', views.runoob),
    url(r'^script/$', views.script),
    url(r'^iftest/$', views.iftest),
    url(r'^fortest/$', views.fortest),
    url(r'^href/$', views.href),

    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),

    path('model/', include('TestModel.urls')),

]
