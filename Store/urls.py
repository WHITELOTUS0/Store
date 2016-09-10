from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from Store import settings,views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    # Admin URL
    url(r'^admin/', include(admin.site.urls)),
    # to protect require login in media
    url(r'^media/(?P<filename>.*)', views.protected_media),
    
    # Translation
#     url(r'^jsi18n/$', javascript_catalog, js_info_dict),
#     url(r'^i18n/', include('django.conf.urls.i18n')),

    # Examples:
    # url(r'^$', 'Store.views.home', name='home'),
    url(r'^dashboard/', include('StockDashboard.urls',namespace="StockDashboard")),
    url(r'^', include('Website.urls',namespace="StockDashboard")),
)

# if settings.DEBUG is True:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
