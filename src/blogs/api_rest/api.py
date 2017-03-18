from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from blogs.api_rest.serializers import BlogSerializer


class BlogsAPI(ListAPIView):
    queryset = User.objects.all().values('username')
    serializer_class = BlogSerializer