from django.apps import AppConfig


class SugConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sug"
    verbose_name = "笔记本推荐"
    label = "suggestion"
