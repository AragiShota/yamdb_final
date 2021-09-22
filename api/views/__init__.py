from .category_view import CategoryViewSet
from .comment_view import CommentViewSet
from .genre_view import GenreViewSet
from .review_view import ReviewViewSet
from .title_view import TitleViewSet
from .user_view import (RegistrationView, RequestForRegistrationView,
                        UserViewSet)

__all__ = [
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    RegistrationView,
    ReviewViewSet,
    RequestForRegistrationView,
    TitleViewSet,
    UserViewSet,
]
