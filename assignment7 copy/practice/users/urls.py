from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('profile/<int:user_id>/detail', profile_detail, name='profile_detail'),
    path('profile/<int:user_id>/edit', profile_edit, name='profile_edit'),
]
