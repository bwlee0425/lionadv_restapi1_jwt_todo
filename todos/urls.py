from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"todos", views.TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', views.register), # localhost:8000/api/register/
    path('', include(router.urls))
]