from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from django.utils.html import format_html
from django.urls import reverse

from api import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Profile._meta.get_fields() if not (field.many_to_many or field.one_to_many or field.many_to_one or field.name=="user")].__add__(["user_link"])

    def user_link(self, obj):
        url = (
            reverse("admin:auth_user_change", args=(obj.user.id,))
        )
        return format_html('<a href="{}">{}</a>', url, obj.user.id)
    pass

@admin.register(models.Wear)
class WearAdmin(ExportActionModelAdmin):
    list_display = [field.name for field in models.Wear._meta.get_fields() if not (field.many_to_many or field.one_to_many or field.many_to_one)].__add__(["type_link","wear_sizes"])
    search_fields = ["id", "name"]
    list_filter = ["name", "cost", "color", ("size", admin.RelatedFieldListFilter)]

    def wear_sizes(self, obj):
        res = list(models.Wear.objects.filter(id=obj.id).values_list("size__name", flat=True))
        return ", ".join(res) if res[0] else ""
    
    def type_link(self, obj):
        url = (
            reverse("admin:api_weartype_change", args=(obj.type.id,))
        )
        return format_html('<a href="{}">{}</a>', url, obj.type)
    
    type_link.short_description = "Type"

    def color_link(self, obj):
        url = (
            reverse(f"admin:api_wearcolor_change", args=(obj.color,))
        )
        return format_html('<a href="{}">{}</a>', url, obj.color.name)

@admin.register(models.WearComment)
class WearCommentAdmin(ExportActionModelAdmin):
    list_display = [field.name for field in models.WearComment._meta.get_fields() if not (field.many_to_many or field.one_to_many or field.many_to_one)].__add__(["wear_obj"])
    search_fields = ["author", "rate", "wear__id"]
    list_filter = ["rate"]

    def wear_obj(self,obj):
        from django.utils.html import format_html
        from django.urls import reverse
        url = (
            reverse("admin:api_wear_change", args=(obj.wear.id, ))
        )
        return format_html(f'<a href="{url}">{obj.wear.name}</a>')
    pass

    wear_obj.short_description = "Wear"


@admin.register(models.WearType)
class WearTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.WearSize)
class WearSizeAdmin(admin.ModelAdmin):
    pass
