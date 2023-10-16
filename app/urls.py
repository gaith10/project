from django.urls import path, include
from django.contrib.auth.views import LoginView  # تأكد من استيراد UserLoginView من ملف العروض الصحيح
from app.forms import UserLoginForm
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('', include('django.contrib.auth.urls'))
]
