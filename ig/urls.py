from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'schemes', views.SchemeViewSet)
router.register(r'compdata', views.ComputationDataViewSet)
router.register(r'idnumbers', views.IdentificationNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('auth/', include('rest_auth.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls')),
]