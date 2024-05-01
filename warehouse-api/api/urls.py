from django.urls import include, path

from rest_framework import routers

from .views import AuthorModelApi, BookModelApi, PublisherModelApi, get_request

router = routers.DefaultRouter()
router.register(r'books', BookModelApi)
router.register(r'authors', AuthorModelApi)
router.register(r'publishers', PublisherModelApi)


urlpatterns = [
    path('', include(router.urls)),
    path('recieve/', get_request)
]
