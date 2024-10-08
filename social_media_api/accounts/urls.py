from django.urls import path
from .views import (RegisterView, 
                    LoginView,
                    FollowUserView,
                    UnfollowUserView, 
                    ListFollowingView,
                    ListUsersView)



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),


    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('following/', ListFollowingView.as_view(), name='list_following'),
    path('users/', ListUsersView.as_view(), name='list_users'),  
]
