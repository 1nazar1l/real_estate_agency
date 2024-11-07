from django.contrib import admin

from .models import Flat, Complaint, Owner

class AdminInline(admin.TabularInline):
    model = Owner.apartments.through
    raw_id_fields = ('owner',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('who_liked',)
    inlines = [AdminInline]

class ModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartments',)

admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ModelAdmin)
admin.site.register(Owner, OwnerAdmin)