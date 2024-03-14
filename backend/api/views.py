from weakref import ref
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.models import Wear, WearComment, WearType
from api.serializers import CreateWearCommentSerializer, UserProfileSerializer, WearCommentSerializer, WearSerializer
from django.db.models import Q, Min, Max
from django.contrib.auth.models import User as AuthUser

from rest_framework.decorators import action
from api.helper import CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

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
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateWearCommentSerializer
        if self.request.method == "GET":
            return WearCommentSerializer
        

    def get_queryset(self):
        queryset = WearComment.objects.all().order_by("-id")
        user_id = self.request.query_params.get("user_id")
        wear_id = self.request.query_params.get("wear_id")
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        if wear_id is not None:
            queryset = queryset.filter(wear=wear_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class User(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        else:
            return [IsAuthenticatedOrReadOnly()]

    def get(self, request, format=None):
        print(request)
        user = request.user
        response = UserProfileSerializer(user, many=False).data 
        return Response({"result":response})
    
    def patch(self, request, format=None):
        data = request.data
        user = AuthUser.objects.get(id=data["id"])
        user.username = data.get("username",user.username)
        profile_data = data.get("profile", None)
        if profile_data:
            user.profile.fio = profile_data.get("fio",user.profile.fio)
            user.profile.geo = profile_data.get("geo",user.profile.geo)
            user.profile.number = profile_data.get("number",user.profile.number)
            user.profile.email = profile_data.get("email",user.profile.email)
        user.save()

        return Response({"result": UserProfileSerializer(user, many=False).data})
    
    def post(self, request):
        data = request.data
        try:
            user = AuthUser.objects.create_user(username=data.get("username"), email=("%s@mail.com" % data.get("username")), password=data.get("password"))
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response({"refresh":str(refresh), "access":str(refresh.access_token)})
        except Exception as e:
            print(e)
            return Response(status=400, data="Error while creating user. Check parameters")
