from rest_framework import serializers
from .models import productMainModel, productColourModel, productImageModel

class serialMain(serializers.ModelSerializer):
    colour = serializers.StringRelatedField(many=True, read_only=True)
    image = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='image-detail')
    class Meta:
        model = productMainModel
        fields = ['id', 'title','description','uniquecode','size','quality','image','colour']

class serialColour(serializers.ModelSerializer):
    class Meta:
        model = productColourModel
        fields = '__all__'

class serialImage(serializers.ModelSerializer):
    class Meta:
        model = productImageModel
        fields = '__all__'
