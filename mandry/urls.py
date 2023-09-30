from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mandry.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('traveller.urls')),
    path('', MainPageView.as_view(), name='main_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
