from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Order, Client
from api.serializers import OrderSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
	queryset = Client.objects.all()
	serializer_class = UserSerializer


class OrderCreateAPIView(CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderAPIView(ListAPIView):
	serializer_class = OrderSerializer

	def get_queryset(self):
		order_id = self.request.GET.get('order_id')
		status = self.request.GET.get('status')
		from_date = self.request.GET.get('from_date')
		to_date = self.request.GET.get('to_date')

		if order_id:
			return Order.objects.filter(order_id=order_id)
		elif status:
			return Order.objects.filter(status=status)
		elif from_date and to_date:
			Order.objects.filter(
				f"{from_date.replace('/', '-')} 00:00:00"
				f"{to_date.replace('/', '-')} 00:00:00"
			)
		# return Order.objects.order_by('-pk')


# class OrderListAPIView(ListAPIView):
# 	queryset = Order.objects.all()
	# serializer_class = OrderSerializer
	# filter_backends = [DjangoFilterBackend]
	# filterset_fields = ['created_at', 'updated_at']
	#
	# def get_queryset(self):
	# 	if Order.objects.filter(
	# 		created_at__range=['2022-01-13T10:13:54.604940Z',
	# 						   '2022-01-13T10:14:02.679469Z']
	# 	):
	# 		return Order.objects.filter(status='Cancelled')


@api_view(['PUT', ])
def order_update_view(request, slug):
	try:
		order = Order.objects.get(slug=slug)

	except Order.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUNT)

	if request.method == 'PUT':
		serializer = OrderSerializer(order, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['success'] = 'update successful'
