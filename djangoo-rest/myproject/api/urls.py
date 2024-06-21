# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
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
]
