from rest_framework.routers import DefaultRouter

from .views import AuthorApiViewSet, BookApiViewSet, PublisherApiViewSet

router = DefaultRouter()
router.register('authors', AuthorApiViewSet)
router.register('books', BookApiViewSet)
router.register('publishers', PublisherApiViewSet)

urlpatterns = router.urls