from django.conf.urls import url
from rest_framework import routers
from .views import MemberViewset, other_activity, other_member

router = routers.DefaultRouter()
router.register(r'get/members', MemberViewset)

urlpatterns = [
    url('member/', other_member, name='member'),
    url('activity/', other_activity, name='activity'),
] + router.urls
