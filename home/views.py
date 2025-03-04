from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    #定义展示的应用列表
    enable_apps = ['introduction', 'suggestion']

    app_links = []
    for app_name in enable_apps:
        app_config = apps.get_app_config(app_name)
        app_links.append({
            'name': app_config.verbose_name,
            'url': app_config.label,
        })

    return render(request, "home/index.html", {'apps': app_links})
