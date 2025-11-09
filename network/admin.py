from django.contrib import admin
from django.utils.html import format_html
from .models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'level_display', 'city', 'supplier_link', 'debt', 'created_at']
    list_filter = ['city', 'country', 'level']
    search_fields = ['name', 'city', 'country']
    actions = ['clear_debt']

    def level_display(self, obj):
        return obj.get_level_display()

    level_display.short_description = 'Тип'

    def supplier_link(self, obj):
        """ Ссылка на поставщика """
        if obj.supplier:
            return format_html('<a href="{}">{}</a>',
                               f'../networknode/{obj.supplier.id}/change/',
                               obj.supplier.name)
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        """ Очистка долга """
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'Задолженность очищена у {updated_count} объектов')

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
