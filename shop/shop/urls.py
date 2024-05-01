from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('shop_app.urls')),
    path('cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
]
