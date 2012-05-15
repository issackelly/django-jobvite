from django.contrib import admin
from django_jobvite.models import Position, Category


class PositionAdmin(admin.ModelAdmin):
    list_display = [
        'job_id',
        'title',
        'category',
        'job_type',
        'location',
    ]

    readonly_fields = [
        'job_id',
        'title',
        'requisition_id',
        'category',
        'job_type',
        'location',
        'date',
        'detail_url',
        'apply_url',
        'description',
        'brief_description',
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    readonly_fields = [
        'name',
        'slug',
        'description',
    ]

admin.site.register(Position, PositionAdmin)
admin.site.register(Category, CategoryAdmin)
