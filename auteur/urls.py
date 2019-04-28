from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('', views.AuteurList.as_view()),
    path('<int:pk>/', views.AuteurDetail.as_view()),
])