from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"books",BookViewSet)

urlpatterns = [
    path("second/", BookList.as_view(), name="book_list"),
    path("", include(router.urls))
]