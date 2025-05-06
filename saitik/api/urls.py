from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'platforms', PlatformViewSet, basename='platform')
router.register(r'games', GameViewSet, basename='games')
router.register(r'developers', DeveloperViewSet, basename='developers')
router.register(r'publishers', PublisherViewSet, basename='wishpublishers')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'posorders', PosOrderViewSet, basename='posorders')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')
urlpatterns += router.urls