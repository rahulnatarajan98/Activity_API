from django.conf.urls import url
from rest_framework import routers
from .views import MemberViewset

router = routers.DefaultRouter()
router.register(r'activity', MemberViewset)

urlpatterns = router.urls