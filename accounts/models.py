from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """カスタムユーザー

    現状、AbstractUserを継承しただけのモデル。
    のちの拡張用に事前に作っておいてる。
    また、djangoの認証用のユーザーはこちらのモデルで置き換えてる
    　詳しくは、settings.AUTH_USER_MODEL
    """
    pass
