from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import Order
from rest_framework import generics, mixins, status
from .models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .serializers import OrderSerializer

class OrderListView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):

    def get_queryset(self):
        return Order.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    serializer_class = OrderSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def main(request):
        orders = Order.objects.all().order_by('-id')
        return render(request, 'order.html', { 'orders': orders })

    def write(request):
    
        if request.method =='POST':
            order = Order(
                ord_ymd = request.POST.get("ORD_YMD"),
                ord_no = request.POST.get('ORD_NO'),

            )

            order.save()  #데이터베이스에 저장! 꼭 save해야함
            return redirect('/')
        
        return render(request, 'order.html')
# Create your views here.
