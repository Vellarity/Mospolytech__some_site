from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

wear_shop_list = views.WearViewSet.as_view({
    'get':'shop_list'
})

wear = views.WearViewSet.as_view({
    'get':'retrieve'
})

comments = views.WearCommentViewSet.as_view({
    'get':'list',
    'post':'create'
})


router = DefaultRouter()
router.register(r'comments', views.WearCommentViewSet, basename='comment')

urlpatterns = [
    #path("shop_list", views.shop_list, name="shop_list"),
    path("wears/shop_list", wear_shop_list, name="wear_shop_list"),
    path("wears/<int:pk>", wear, name="wear"),
    
    path("filters/types", views.filters_types),
    path("filters/costs", views.filters_costs),

    #path("comments", comments, name="comments_list")
] + router.urls