from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name = 'register'), 
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('home/', views.home, name = 'home'),
    path('home/my-information/', views.my_info, name = 'my_info'),
    path('home/adresses', views.profile_adress, name = "adresses"),
    path('home/adresses/add', views.add_adress, name = "add_adress"),
    path('home/adresses/change-adress/<int:adress_id>', views.change_adress, name = 'change_adress'),
    path('home/adresses/delete-adress/<int:adress_id>', views.delete_adress, name = 'delete_adress'),
    path('home/contacts', views.change_contacts_preferences, name = 'contacts'),
    path('home/favourities', views.fav_goods, name = 'fav_goods'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset/password_reset.html",
        email_template_name = 'accounts/password_reset/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done')),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset/password_reset_form.html",
        success_url = reverse_lazy('accounts:password_reset_complete')), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset/password_reset_done.html"), 
        name="password_reset_complete"),
]