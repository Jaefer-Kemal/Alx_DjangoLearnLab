from django.urls import path
from .views import register, index, profile_view
from django.contrib.auth import views as auth_views
from . import views as blog_views
# Define URL patterns in blog/urls.py
# to handle paths for login (/login),
# logout (/logout), registration (/register),
# and profile management (/profile).

# Map the CRUD views to appropriate URLs in blog/urls.py.
# Ensure each URL is intuitive and descriptive, like /posts/ for the list,
# /posts/new/ for creating a post,
# /posts/<int:pk>/ for viewing details,
# /posts/<int:pk>/edit/ for editing, and 
# /posts/<int:pk>/delete/ for deletion.

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login",),
    path("logout/",auth_views.LogoutView.as_view(template_name="blog/logout.html", http_method_names=["get", "post"]),name="logout",),
    path('profile/', profile_view, name='profile'),
    path('post', blog_views.PostListView.as_view(), name='post-list'),  # URL for the list view
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),  # URL for detail view
    path('post/new/', blog_views.PostCreateView.as_view(), name='post-create'),  # URL for create view
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='post-update'),  # URL for update view
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),  
    path('post/<int:post_id>/comments/new/', blog_views.add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', blog_views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', blog_views.CommentDeleteView.as_view(), name='delete-comment'),
    
]

