from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from mandry.views import MainPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('trip/', include('trip.urls')),
    path('favicon.ico', RedirectView.as_view(url='/media/favicon.ico')),
    path('accounts/', include('traveller.urls')),
    path('', MainPageView.as_view(), name='main_page'),
    path('trips/', include('trip.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
