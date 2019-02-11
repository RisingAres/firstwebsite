from django.urls import path
from .views import MainViews

urlpatterns = [
    path('', MainViews.as_view(), name='main')
]
