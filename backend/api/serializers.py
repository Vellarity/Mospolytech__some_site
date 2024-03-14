from dataclasses import fields
from importlib.metadata import files
from django.conf import settings
from rest_framework import  serializers
from django.contrib.auth.models import User
from api.models import Wear, WearComment, WearSize, Profile


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    
class WearSizeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WearSize
        fields = '__all__'

class WearSerializer(DynamicFieldsModelSerializer):
    image_url = serializers.SerializerMethodField()
    size = WearSizeSerializer(read_only=True, many=True)
    color = serializers.SerializerMethodField()
    type = serializers.StringRelatedField()

    class Meta:
        model = Wear
        fields = '__all__'

    @staticmethod
    def get_color(obj):
        return Wear.COLORS[obj.color]
 
    @staticmethod
    def get_image_url(obj):
        return obj.image.url if obj.image else None 

class CommentUserSerializer(DynamicFieldsModelSerializer):
    fio = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "fio"]

    @staticmethod
    def get_fio(obj):
        return obj.profile.fio

class CommentWearSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Wear
        fields = ["id","name"]

class WearCommentSerializer(DynamicFieldsModelSerializer):
    #wear = serializers.SlugRelatedField("id", read_only=True)
    user = CommentUserSerializer(many=False)
    wear = CommentWearSerializer(many=False)

    class Meta:
        model = WearComment
        fields = '__all__'

class CreateWearCommentSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WearComment
        fields = '__all__'

class ProfileSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]

    def to_representation(self, instance):
        return super().to_representation(instance) if instance else {"fio":"", "geo":"", "number":"", "email":""}

class UserProfileSerializer(DynamicFieldsModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ["id", "username", "profile"]

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        if not repr["profile"]:
            repr["profile"] = {"fio":"", "geo":"", "number":"", "email":""}
        return repr