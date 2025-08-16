from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignupView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('', include(router.urls)),
]