from django.contrib import admin
from django.urls import path, include
from application.serializers import MapasSerializer
from application.views import MapasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Mapas', MapasViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
