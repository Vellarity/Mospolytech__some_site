from django.contrib import admin
from import_export.admin import ExportActionModelAdmin

from api import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Wear)
class WearAdmin(ExportActionModelAdmin):
    list_display = [field.name for field in models.Wear._meta.get_fields() if not (field.many_to_many or field.one_to_many or field.many_to_one)].__add__(["type_link","wear_sizes"])

    def wear_sizes(self, obj):
        res = list(models.Wear.objects.filter(id=obj.id).values_list("size__name", flat=True))
        return ", ".join(res) if res[0] else ""
    
    def type_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse
        from django.utils.http import urlencode
        url = (
            reverse(f"admin:api_weartype_change", args=(obj.type.id,))
        )
        return format_html('<a href="{}">{}</a>', url, obj.type)
    
    type_link.short_description = "Type"

    def color_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse
        from django.utils.http import urlencode
        url = (
            reverse(f"admin:api_wearcolor_change", args=(obj.color,))
        )
        return format_html('<a href="{}">{}</a>', url, obj.color.name)

@admin.register(models.WearComment)
class WearCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.WearType)
class WearTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.WearSize)
class WearSizeAdmin(admin.ModelAdmin):
    pass
