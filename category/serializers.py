from rest_framework import serializers

from category.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        children = instance.children.all()
        if children:
            repr['children'] = CategoryListSerializer(children, many=True).data

        return repr