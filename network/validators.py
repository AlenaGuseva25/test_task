from rest_framework import serializers

def validate_product_release_date(value):
    """ Валидация даты выхода продукта """
    from datetime import date
    if value > date.today():
        raise serializers.ValidationError("Дата выхода продукта не должна быть позже нынешней даты")
    return value

def validate_debt(value):
    """ Валидация задолженности (НЕ МОЖЕТ БЫТЬ ОТРИЦАТЕЛЬНОЙ) """
    if value < 0:
        raise serializers.ValidationError("Задолженность не может быть отрицательной")
    return value