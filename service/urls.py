from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # router

router.register('', views.serviceViewset) # router antena
urlpatterns = [
    path('', include(router.urls)),
]