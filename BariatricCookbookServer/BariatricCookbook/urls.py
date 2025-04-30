from django.urls import path
from .views import ProfileDetailView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/me/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
