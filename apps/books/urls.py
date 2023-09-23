from django.urls import path, include

from rest_framework import routers

from apps.books.views import BookViewSet, SectionViewSet


from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Book Writer Platform API')

router = routers.DefaultRouter()
router.register('book', BookViewSet)
router.register('section', SectionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]