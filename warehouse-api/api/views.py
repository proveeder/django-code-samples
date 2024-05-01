from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import Author, Book, Publisher
from .serializers import AuthorSerializer, BookSerializer, GetRequestSerializer, PublisherSerializer


class BookModelApi(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorModelApi(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherModelApi(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


@api_view(['POST'])
def get_request(request):
    data = JSONParser().parse(request)
    serializer = GetRequestSerializer(data=data)
    if serializer.is_valid():
        queryset = Book.objects.filter(name=serializer.data['name'])
        queryset[0].delete()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
