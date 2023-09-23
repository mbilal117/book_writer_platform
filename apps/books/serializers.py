from rest_framework import serializers

from apps.books.models import Books, Sections


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('url', 'id', 'name', 'sections')
        depth = 1


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class SectionsSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Sections
        fields = ['url', 'id', 'name', 'book', 'parent', 'children']


    def to_representation(self, instance):
        self.fields['children'] = SectionsSerializer(many=True, read_only=True)
        return super(SectionsSerializer, self).to_representation(instance)





