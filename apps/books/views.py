from apps.books.models import Books, Sections
from apps.books.serializers import BooksSerializer, SectionsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from apps.common.permissions import IsOwnerOrReadOnly


class BookViewSet(ModelViewSet):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class SectionViewSet(ModelViewSet):
	queryset = Sections.objects.all()
	serializer_class = SectionsSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
