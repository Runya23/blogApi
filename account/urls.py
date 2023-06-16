from django.urls import path, include
from account import views
from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import LoginView 

from account import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('', include(router.urls)),
    # path('', views.UserListView.as_view()),
    # path('<int:pk>/', views.UserDetailView.as_view()),
]