from django.urls import path

from . import views

urlpatterns = [
    path("shop_list", views.shop_list, name="shop_list"),
    path("filters/types", views.filters_types),
    path("filters/costs", views.filters_costs),
]