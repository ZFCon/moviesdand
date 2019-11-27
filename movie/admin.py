from django.contrib import admin
from .models import *

admin.site.site_header = 'Moviesdand Admin'

class ActInline(admin.StackedInline):
    model = Act
    extra = 0
    

class FrameInline(admin.TabularInline):
    model = Frame
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'requested', 'timestamp')
    search_fields = ('title', 'year')
    list_filter = ('timestamp', )
    ordering = ('-requested', '-views')
    inlines = [ActInline, FrameInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_comment', 'timestamp')
    list_filter = ('timestamp', )
    def get_comment(self, obj):
        return obj.comment[:20]

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Comment, CommentAdmin)
