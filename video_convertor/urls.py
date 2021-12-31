from rest_framework.authtoken import views
from rest_framework.urls import path

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token)
]