from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
<<<<<<< HEAD

router = DefaultRouter()
router.register(r"todos", views.TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', views.register), # localhost:8000/api/register/
    path('', include(router.urls))
=======
from .views import UserList, UserDetail

router = DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', views.register), # localhost:8000/api/register/
    path('', include(router.urls)),
    path('users/', UserList.as_view(), name='user-list'),  # 모든 사용자 조회
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # 특정 사용자 조회
>>>>>>> fcba87d9aba674431dd54ea4b932190fa2b6c000
]