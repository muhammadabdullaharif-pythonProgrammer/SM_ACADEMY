"""
URL configuration for Academy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Academy import views
from django.contrib.auth import views as auth_views
from django.conf import settings # for images settings
from django.conf.urls.static import static  # for image 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('admission/',views.admission),
    path('login/',views.login_view, name='login'),
    path('contact/',views.contact),
    path('signup/',views.signup_view),
    # for forgot password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_done.html'), name='password_reset_complete'),
    
]   


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
