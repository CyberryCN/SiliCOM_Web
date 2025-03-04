# introduction/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Operator

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('op_id', 'management_name', 'photo_preview', 'management_time')
    list_filter = ('management_campus',)
    search_fields = ('management_name', 'op_id')
    readonly_fields = ('photo_preview',)

    fieldsets = (
        ('基本信息', {
            'fields': (
                'op_id', 
                'management_name',
                'management_campus',
                'management_time'
            )
        }),
        ('详细信息', {
            'fields': (
                'photo',
                'photo_preview',
                'introduction'
            )
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height: 100px; border-radius: 4px;">',
                obj.photo.url
            )
        return "暂无照片"
    photo_preview.short_description = "照片预览"
