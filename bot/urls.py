from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/images/favicon.ico')),
]
