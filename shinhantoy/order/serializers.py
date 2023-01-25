from rest_framework import serializers
from .models import Order
import datetime

class OrderSerializer(serializers.ModelSerializer):
    ord_no = serializers.SerializerMethodField()
    ord_ymd = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_ord_no(self, obj):
        return obj.ord_no


    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    Order = serializers.HiddenField(default = serializers.CurrentUserDefault(),
    required = False)


    def validate_order(self,value):
        if not value.is_authenticated:
            raise serializers.ValidationError('order is required')
        return value
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'order': {'required' : False}}