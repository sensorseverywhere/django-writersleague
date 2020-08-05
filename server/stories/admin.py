from django.contrib import admin

from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'genre', 'votes')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('votes',)
