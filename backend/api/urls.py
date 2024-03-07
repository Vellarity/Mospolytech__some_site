from django.urls import path

from . import views

wear_shop_list = views.WearViewSet.as_view({
    'get':'shop_list'
})

wear = views.WearViewSet.as_view({
    'get':'retrieve'
})

comment_list = views.WearCommentViewSet.as_view({
    'get':'list'
})

urlpatterns = [
    #path("shop_list", views.shop_list, name="shop_list"),
    path("wears/shop_list", wear_shop_list, name="wear_shop_list"),
    path("wears/<int:pk>", wear, name="wear"),
    
    path("filters/types", views.filters_types),
    path("filters/costs", views.filters_costs),

    path("comments", comment_list, name="comments_list")
]