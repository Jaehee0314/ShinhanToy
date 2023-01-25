from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

#class OrderListSerializer(serializers.ModelSerializer):
   # Order = serializers.HiddenField(default = serializers.CurrentUserDefault(),
   # required = False)


    #def validate_order(self,value):
        #if not value.is_authenticated:
          #  raise serializers.ValidationError('order is required')
       # return value
    #class Meta:
       # model = Order
       # fields = '__all__'
      #  extra_kwargs = {'order': {'required' : False}}