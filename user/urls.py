from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.sign_in, name='signin'),

    path('signout/', views.logout, name='logout'),
    # path('changepassword/<username>/', views.change_password, name='change-password'),
    # path('users/<username>/', views.profile, name='profile'),
    # path('ajax/profile/edit/<username>/', views.edit_profile, name="edit-profile")
]+ static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)