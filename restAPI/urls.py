from django.urls import include, path
from rest_framework import routers
from API import views
from django.conf import settings
from django.conf.urls.static import static

from API.views import ItemViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
    path(r'^api/', include(router.urls)),
    path(r'^admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)