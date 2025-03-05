from django.contrib import admin
from .models import Activity, Sign, Comment

# Register your models here.
@admin.register(Activity)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'title')
    search_fields = ('title', 'activity_id')
admin.site.register(Sign)
admin.site.register(Comment)