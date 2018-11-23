from django.contrib import admin
from django.urls import path, include
from application.serializers import LogisticaSerializer
from application.views import LogisticaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Logistica', LogisticaViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
