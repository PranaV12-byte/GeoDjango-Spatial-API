from rest_framework.routers import DefaultRouter
from .views import BoundaryViewsets

router = DefaultRouter()
router.register(
    prefix="api/v1/boundaries", viewset=BoundaryViewsets, basename="boundary"
)

urlpatterns = router.urls
