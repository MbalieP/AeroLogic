from django.contrib import admin
from .models import BoardingPass


@admin.register(BoardingPass)
class BoardingPassAdmin(admin.ModelAdmin):
    list_display = ('flight', 'passenger', 'seat_code', 'checked_in_at')
    list_filter = ('flight',)
    search_fields = ('passenger__first', 'passenger__last', 'seat_code')
