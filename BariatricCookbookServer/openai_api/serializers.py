from rest_framework import serializers

class MealPlanSerializer(serializers.Serializer):
    preferences = serializers.DictField(child=serializers.CharField(default=''), required=False)
    days = serializers.IntegerField(min_value=1, default=7)
    mealsPerDay = serializers.IntegerField(min_value=1, default=3)

