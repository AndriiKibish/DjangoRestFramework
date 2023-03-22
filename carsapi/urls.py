from django.urls import include, path
from rest_framework import routers
from carsapi import views


router = routers.SimpleRouter()
router.register(r'car', views.CarsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
