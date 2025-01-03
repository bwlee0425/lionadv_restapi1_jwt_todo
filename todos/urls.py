from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserList, UserDetail

router = DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', views.register), # localhost:8000/api/register/
    path('', include(router.urls)),
    path('users/', UserList.as_view(), name='user-list'),  # 모든 사용자 조회
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # 특정 사용자 조회
]