from django.urls import re_path, path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import forms

urlpatterns = [
    # post views
    re_path(r'^login/$', LoginView.as_view(), name="login"),
    re_path(r'^logout/$', LogoutView.as_view(), name="logout"),
    re_path(r'^signup/$', forms.SignUpView.as_view(), name="signup")
    #re_path(r'^logout/$', LogoutView.as_view(template_name='main/logged_out.html'), name="logout"),
]