from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at')  # 필요한 필드 추가
    search_fields = ('title', 'content')  # 검색할 필드 추가
    list_filter = ('is_completed', 'user')  # 필터링할 필드 추가