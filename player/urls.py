from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView

from .views import home, SignUpView

urlpatterns = [
    url(r'home$', home,
        name="player_home"),
    url(r'login$',
        LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="player_logout"),
    url(r'signup$',
        SignUpView.as_view(),
        name='player_signup')
]
