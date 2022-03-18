from django.urls import path
 
from . import views
 
urlpatterns = [
    path('hello/', views.hello),
    path('runoob/', views.runoob),
    path('script/', views.script),
    path('iftest/', views.iftest),
    path('fortest/', views.fortest),
]