from django.urls import path
from .views import user_login

app_name = "accounts"

urlpatterns = [
    path('login/',view=user_login,name='user_login')
]
