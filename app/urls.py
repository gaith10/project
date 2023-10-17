from django.urls import path, include
from django.contrib.auth.views import LoginView  # تأكد من استيراد UserLoginView من ملف العروض الصحيح
from app.forms import UserLoginForm
from app.views import RegisterView,edit_profile
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('', include('django.contrib.auth.urls'))
]
