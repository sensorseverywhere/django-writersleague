from django.contrib import admin

from .models import ContentBlock, ContentBlockImage, PageTemplateTag, NewsItem

# Register your models here.
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'tags', 'content')
    list_filter = ('title', 'active',)
    list_editable = ('title', 'tags', 'content')
    list_display_links = None
    search_fields = ('title',)

admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ContentBlockImage)
admin.site.register(PageTemplateTag)
admin.site.register(NewsItem)
