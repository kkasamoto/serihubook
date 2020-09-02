from django.db import models


class Serihu(models.Model):
    """ 様々な人・キャラが発した言葉やセリフを表すモデル

    誰かの心に残る名言、はたまた迷言までなんでも可。

    Parameter
    ---------
    serihu: str
        セリフ。500字以内。
    owner: str
        セリフを発した人・キャラ。30字以内
    created_by: str
        このセリフを登録したユーザー（現バージョンでは、すべて管理者）
    created_at: datetime
        このセリフが登録された日時
    updated_by: datetime
        このセリフが更新された日時
    """
    serihu = models.CharField(max_length=500)
    owner = models.CharField(max_length=30)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Serihu<id={self.id}, serihu={self.serihu[:5]}..., owner={self.owner}>'
