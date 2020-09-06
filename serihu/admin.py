from django import forms
from django.contrib import admin

from serihu.models import Serihu


class AdminSerihuForm(forms.ModelForm):
    serihu = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Serihu
        fields = ['serihu', 'owner', 'created_by']


class SerihuAdmin(admin.ModelAdmin):
    form = AdminSerihuForm


admin.site.register(Serihu, SerihuAdmin)
