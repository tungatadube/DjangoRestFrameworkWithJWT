from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from api.views import SubscriberViewSet

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
urlpatterns = router.urls + [
    url(r'^login/', obtain_jwt_token, name='jwt_login'),




]


