from django.urls import path

from api.views import UserCreateAPIView, OrderCreateAPIView, OrderAPIView, OrderUpdateAPIView

urlpatterns = [
	path('user/create/', UserCreateAPIView.as_view()),
	path('order/<int:pk>/', OrderAPIView.as_view()),
	path('', OrderAPIView.as_view()),
	path('filter/', OrderAPIView.as_view()),
	path('update/<int:pk>/', OrderUpdateAPIView.as_view()),
	path('order/create/', OrderCreateAPIView.as_view()),

]
