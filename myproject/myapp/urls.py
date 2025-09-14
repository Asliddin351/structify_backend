"""
URL configuration for the API layer of myapp.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapp.views import (
    ForumViewSet, CommentViewSet, BookViewSet, ArticleViewSet,
    UserViewSet, RegisterView, CategoryViewSet,
    ArticlesReportJSON, ArticlesReportCSV,
    serve_protected_file
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'forums', ForumViewSet, basename='forum')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'books', BookViewSet, basename='book')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected-file/<path:file_path>/', serve_protected_file, name='serve_protected_file'),  # Добавлен маршрут для защищённых файлов

    # Reports
    path('reports/articles/', ArticlesReportJSON.as_view(), name='articles_report_json'),
    path('reports/articles.csv', ArticlesReportCSV.as_view(), name='articles_report_csv'),
]