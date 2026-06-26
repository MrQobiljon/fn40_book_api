from rest_framework.routers import DefaultRouter

from .views import AuthorApiViewSet, BookApiViewSet

router = DefaultRouter()
router.register('authors', AuthorApiViewSet)
router.register('books', BookApiViewSet)

urlpatterns = router.urls