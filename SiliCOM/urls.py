"""
URL configuration for SiliCOM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from home.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="root-index"),
    path("admin/", admin.site.urls),
    path("donation/",include("donation.urls")),
    path("document/", include("document.urls")),
    path("introduction/", include("intro.urls")),
    path("recruitment",include("recruiment.urls")),
    path("suggestion/", include("sug.urls")),
    path("service/", include("service.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
