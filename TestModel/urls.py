from django.conf.urls import url

from TestModel.model_views import model_index

urlpatterns = [

    url(r'^index/$', model_index),
]
