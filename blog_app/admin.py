from django.contrib import admin

from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag_list')
    list_display_links = ('id', 'title')

    def tag_list(self, objects):
        return ", ".join(obj.name for obj in objects.tags.all())


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
