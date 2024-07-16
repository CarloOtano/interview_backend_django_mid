
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, DeactivateOrderView, ActivateOrderView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('deactivate/<int:id>', DeactivateOrderView.as_view(), name='order-deactivate'),
    path('activate/<int:id>', ActivateOrderView.as_view(), name='order-activate'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]