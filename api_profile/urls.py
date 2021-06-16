from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_profile import views


router = DefaultRouter()
# we can define base_name or rest_framework consider queryset name
router.register('hello', viewset=views.HelloViewSet, basename='hello-viewset')
router.register('profile', viewset=views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns = [
    path('login/', views.LoginUserApiView.as_view()),
    path('', include(router.urls)),

]
