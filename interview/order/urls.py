
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListBetweenDatesView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('between/<str:startDate>/<str:embargoDate>/', OrderListBetweenDatesView.as_view(), name='order-between-dates'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]