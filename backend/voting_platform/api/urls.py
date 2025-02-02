from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.users import UserViewSet, CustomSignup
from authemail import views


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('auth/signup', CustomSignup.as_view(), name='custom-signup'),
    path('auth/signup/', CustomSignup.as_view(), name='custom-signup'),

    path('auth/verify-email/', views.SignupVerify.as_view(),
        name='authemail-signup-verify'),
    path('auth/login/', views.Login.as_view(), name='authemail-login'),
    path('auth/logout/', views.Logout.as_view(), name='authemail-logout'),

    path('auth/password/reset/', views.PasswordReset.as_view(),
        name='authemail-password-reset'),

    path('auth/password/reset/verify/', views.PasswordResetVerify.as_view(),
        name='authemail-password-reset-verify'),
    path('auth/password/reset/verified/', views.PasswordResetVerified.as_view(),
        name='authemail-password-reset-verified'),
    path('email/change/', views.EmailChange.as_view(),
         name='authemail-email-change'),
    path('email/change/verify/', views.EmailChangeVerify.as_view(),
         name='authemail-email-change-verify'),

    path('password/change/', views.PasswordChange.as_view(),
        name='authemail-password-change'),
]
