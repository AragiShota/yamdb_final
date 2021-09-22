from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    RegistrationView, RequestForRegistrationView,
                    ReviewViewSet, TitleViewSet, UserViewSet)

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews for title'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments for review'
)
v1_router.register(
    (r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/'
     r'comments/(?P<comment_id>\d+)'),
    CommentViewSet,
    basename='current comment for review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)',
    ReviewViewSet,
    basename='current review for title'
)
v1_router.register('categories', CategoryViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/email/', RequestForRegistrationView.as_view(),
         name='registration'),
    path('v1/auth/token/', RegistrationView.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
