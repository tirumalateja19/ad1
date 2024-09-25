from django.urls import path

from .views import *

urlpatterns = [
    path('main/login/',login_view,name='login'),
    path('main/',main_view,name='main'),
    path('',main_view),
    path('view/',view)
]
