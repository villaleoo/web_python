from django.urls import path
from users.views import login,check_in,edit_profile, EditPassword
from django.contrib.auth.views import LogoutView

app_name='users'

urlpatterns = [
    path('login',login, name='login' ),
    path('checkin',check_in, name="checkin"),
    path('expired-sesion', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('edit-password',EditPassword.as_view() , name='edit_psw'),
    path("edit-profile",edit_profile, name="edit_data")
]
