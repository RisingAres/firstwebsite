from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from .views import RegistrationView, LoginView

urlpatterns = [
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login_view'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('main')), name='logout_view'),
]
