from django.urls import path
from .api import post_list,post_create,post_list_profile


urlpatterns = [
    path('',post_list,name='post'),
    path('create/',post_create,name='post_create'),
    #profile
    path('profile/<uuid:id>/',post_list_profile,name='post_list_profile')
]
