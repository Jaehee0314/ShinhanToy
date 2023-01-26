from rest_framework import generics, mixins
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
from .models import Order, Comment

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        # 인자값 받아서 filter
        return Order.objects.all().order_by('id')

        # ord_no = self.request.query_params.get('ord_no')
        # if ord_no:
        #    orders = orders.filter(pk=orders.pk)
        #       # if 'name' in self.request.query_params: # 딕셔너리
        #    # name = self.request.query_params['name']
        #    # products = products.filter(name__contains = name)
        # return orders.order_by('id')
 
    def get(self, request, *args, **kwargs):
    
        return self.retrieve(request, args, kwargs)
       
        #Queryset
        #serialize
        #return response


    def post(self,request, *args, **kwargs):

        return self.create(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentWriteView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
): 
    serializer_class = CommentCreateSerializer

    def post(self,request, *args, **kwargs):
        return self.create(request, args, kwargs)

