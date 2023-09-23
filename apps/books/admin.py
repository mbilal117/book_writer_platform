from django.contrib import admin

from apps.books.models import Books, Sections


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    pass
