from django.urls import path

from api.views import UserCreateAPIView, OrderCreateAPIView, OrderAPIView

urlpatterns = [
	# path('order/<int:pk>/clients/<int:pk>/' )
	path('user/create/', UserCreateAPIView.as_view()),
	path('order/<int:pk>/', OrderAPIView.as_view()),
	path('order/create/', OrderCreateAPIView.as_view()),

]
