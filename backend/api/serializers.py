from rest_framework import  serializers

from api.models import Wear, WearComment, WearSize


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

class WearCommentSerializer(DynamicFieldsModelSerializer):
    #wear = serializers.SlugRelatedField("id", read_only=True)

    class Meta:
        model = WearComment
        fields = '__all__'