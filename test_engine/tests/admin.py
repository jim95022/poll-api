from django.contrib import admin
from .models import *


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'created', 'title', 'start_date', 'end_date', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('description',  'end_date')
    list_filter = ('created', 'start_date', 'end_date')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll_name', 'body', 'type_qstn')
    list_display_links = ('poll_name',)
    list_editable = ('type_qstn', 'body')
    search_fields = ('type_qstn',)


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'slug','result')
    list_display_links = ('slug',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Results, ResultsAdmin)