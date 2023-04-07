from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from myapp.views import home, send_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', home, name='home'),
    path('send-message/', send_message, name='send-message'),
]
