from django.urls import path
from django.contrib.auth import views as auth_views
from traveller.views import (
    SignUpView,
    ProfileDetailView, update_profile, leave_comment
)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='traveller/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(template_name='traveller/password_change.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='traveller/password_change_done.html'),
        name='password_change_done'
    ),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('leave-comment/<int:user_id>/', leave_comment, name='leave_comment'),

]
