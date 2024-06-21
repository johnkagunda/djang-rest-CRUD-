from django.contrib import admin
from django.urls import path, include

from api import views

from api.views import HelloWorldView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
 path('hello/', HelloWorldView.as_view(), name='hello_world'),
     path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('dj_rest_auth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # URLs for Item model
    path('items/', views.ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/', views.ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),

    # URLs for student model
    path('students/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),

    # URLs for administration model
    path('administration/', views.AdministrationCreateView.as_view(), name='administration-create'),
    path('administration/<int:pk>/', views.AdministrationRetrieveUpdateDestroyView.as_view(), name='administration-detail'),

    # Example path for getData function
    path('getData/', views.getData, name='get-data'),

     path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]