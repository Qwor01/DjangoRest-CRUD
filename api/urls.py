from django.urls import path,include
from rest_framework import routers
from api import views

routers=routers.DefaultRouter()
routers.register(r'programmers',views.ProgrammerViewset)

urlpatterns = [
    path('',include(routers.urls))
]