from django.contrib import admin
from .models import IrOpsEvent, ReaccommodationSuggestion


@admin.register(IrOpsEvent)
class IrOpsEventAdmin(admin.ModelAdmin):
    list_display = ('flight', 'type', 'reason', 'created_at')
    list_filter = ('type', 'flight')


@admin.register(ReaccommodationSuggestion)
class ReaccommodationSuggestionAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'from_flight', 'to_flight', 'score', 'status')
    list_filter = ('status',)
    search_fields = ('passenger__first', 'passenger__last')
