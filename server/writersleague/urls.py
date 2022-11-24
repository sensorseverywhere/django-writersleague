"""writersleague URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('plotify/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('user.urls')),
    path('', include('cart.urls')),
    path('', include('orders.urls')),
    path('', include('pages.urls')),
    path('', include('payments.urls')),
    path('', include('products.urls')),
    path('', include('stories.urls')),
    path('martor/', include('martor.urls')),
]

if not settings.DEBUG:
    urlpatterns += re_path('^static/(?P<path>.*)$', serve, dict(document_root=settings.STATIC_ROOT)),

if settings.DEBUG:
    import debug_toolbar
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
