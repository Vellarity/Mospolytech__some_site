from django.http import JsonResponse
from rest_framework.decorators import api_view
from api.models import Wear, WearComment, WearType
from api.serializers import WearCommentSerializer, WearSerializer
from django.db.models import Q, Min, Max

from rest_framework.decorators import action
from api.helper import CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response

#!!! SOF CSRF THEME

import json
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'username': request.user.username})


#!!! EOF CSRF THEME

# Create your views here.


@api_view(['GET'])
def shop_list(request):
    try:
        data=request.query_params
        paginator = CustomPagination()

        maxCost_Q = Q()
        colors_Q = Q()
        types_Q = Q()
        if data.get("maxCost", '0') != '0':
            maxCost_Q = Q(cost__lte=data["maxCost"])
        if len(data.getlist("colors", [])) != 0:
            colors_Q = Q(color__in=data.getlist("colors"))
        if len(data.getlist("types", [])) != 0:
            types_Q = Q(type__id__in=data.getlist("types")) 
        res = Wear.objects.prefetch_related(
            'size'
        ).filter(
            colors_Q
            & types_Q
            & Q(cost__gte=data.get("minCost","0")) 
            & maxCost_Q
            & Q(name__icontains=data.get("searchParam",""))
        )

        res = paginator.paginate_queryset(res, request)
        res = WearSerializer(res, many=True).data
    except Exception as e:
        raise(e)
    return paginator.get_paginated_response(res)

@api_view(["GET"])
def filters_types(request):
    try:
        res = WearType.objects.values("id", "name")
    except Exception as e:
        return JsonResponse({"error":True})
    return JsonResponse({"error":False, "data": list(res)})

@api_view(["GET"])
def filters_costs(request):
    try:
        min = Wear.objects.aggregate(Min("cost", default = 0))["cost__min"]
        max = Wear.objects.aggregate(Max("cost", default = 0))["cost__max"]
    except Exception as e:
        raise
    return JsonResponse({"error":False, "data": {"min":min, "max":max}})

class WearViewSet(viewsets.ModelViewSet):
    queryset = Wear.objects.select_related("type")
    serializer_class = WearSerializer

    @action(methods=["get"], detail=False)
    def shop_list(self, request):
        try:
            data=request.query_params
            paginator = CustomPagination()

            maxCost_Q = Q()
            colors_Q = Q()
            types_Q = Q()
            if data.get("maxCost", '0') != '0':
                maxCost_Q = Q(cost__lte=data["maxCost"])
            if len(data.getlist("colors", [])) != 0:
                colors_Q = Q(color__in=data.getlist("colors"))
            if len(data.getlist("types", [])) != 0:
                types_Q = Q(type__id__in=data.getlist("types")) 
            res = Wear.objects.prefetch_related(
                'size'
            ).filter(
                colors_Q
                & types_Q
                & Q(cost__gte=data.get("minCost","0")) 
                & maxCost_Q
                & Q(name__icontains=data.get("searchParam",""))
            )

            res = paginator.paginate_queryset(res, request)
            res = WearSerializer(res, many=True).data
        except Exception as e:
            raise(e)
        return paginator.get_paginated_response(res)
    

class WearCommentViewSet(viewsets.ModelViewSet):
    serializer_class=WearCommentSerializer

    def get_queryset(self):
        queryset = WearComment.objects.all()
        user_id = self.request.query_params.get("user_id")
        wear_id = self.request.query_params.get("wear_id")
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        if wear_id is not None:
            queryset = queryset.filter(wear=wear_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)