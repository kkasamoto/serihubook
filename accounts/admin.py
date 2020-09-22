"""
管理用サイトで、カスタムユーザーを管理するための設定モジュール
"""
from django.contrib import admin

from .models import User

admin.site.register(User)
