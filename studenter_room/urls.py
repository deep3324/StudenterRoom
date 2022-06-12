"""studenter_room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
# from studentApp.sitemaps import Static_Sitemap
# from django.contrib.sitemaps.views import sitemap

admin.site.site_header = "Studenter Room Admin"
admin.site.site_title = "Studenter Room Admin Portal"
admin.site.index_title = "Studenter Room"

# sitemaps = {
#     'static': Static_Sitemap(),
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("studentApp.urls")),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'studentApp.views.error_404'
