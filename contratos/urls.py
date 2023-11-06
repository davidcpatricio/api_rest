from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contratos/(?P<contrato_id>.+)/entidades', views.EntidadeDeContratoViewSet, basename='abc')
router.register(r'entidades/(?P<entidade_id>.+)/contratos', views.EntidadeDeContratoViewSet, basename='abc')
router.register(r'entidades', views.EntidadeViewSet)
router.register(r'moradas', views.MoradaViewSet)
router.register(r'contratos', views.ContratoViewSet)
router.register(r'entidades_de_contratos', views.EntidadeDeContratoViewSet, basename='xyz')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
