from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    """ Сериализатор для работы с сетью, задолженность нельзя изменить (ДОСТУПНА ТОЛЬКО ДЛЯ ПРОСМОТРА) """
    level_display = serializers.CharField(
        source='get_level_display',
        read_only=True
    )
    supplier_name = serializers.CharField(
        source='supplier.name',
        read_only=True
    )

    class Meta:
        model = NetworkNode
        fields = [
            'id', 'name', 'level', 'level_display', 'supplier', 'supplier_name',
            'debt', 'created_at', 'email', 'country', 'city', 'street',
            'house_number', 'product', 'product_model', 'product_release_date'
        ]
        read_only_fields = ['debt']


class NetworkNodeCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания/обновления (БЕЗ ЗАДОЛЖЕННОСТИ)"""

    class Meta:
        model = NetworkNode
        fields = [
            'name', 'level', 'supplier', 'email', 'country', 'city',
            'street', 'house_number', 'product', 'product_model', 'product_release_date'
        ]

    def validate(self, data):
        """Валидация иерархии"""
        level = data.get('level')
        supplier = data.get('supplier')

        if level == 0 and supplier:
            raise serializers.ValidationError("Завод не может иметь поставщика")

        if level in [1, 2] and not supplier:
            raise serializers.ValidationError("Розничная сеть и ИП должны иметь поставщика")

        return data


class NetworkNodeFilterSerializer(serializers.ModelSerializer):
    """ Сериализатор для списка с фильтрацией """
    level_display = serializers.CharField(source='get_level_display', read_only=True)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'level_display', 'country', 'city', 'debt']