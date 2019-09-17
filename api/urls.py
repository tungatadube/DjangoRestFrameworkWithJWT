from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from api.views import SubscriberViewSet

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
urlpatterns = router.urls


