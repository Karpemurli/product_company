from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Login (project level)
    path('api/login/', TokenObtainPairView.as_view()),

    # Register (app level)
    path('api/auth/', include('accounts.urls')),
]
