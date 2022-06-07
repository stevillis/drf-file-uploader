from django.shortcuts import render

from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import DocumentVersion
from api.serializers import DocumentVersionSerializer


class FileUploaderView(APIView):
    parser_class = (MultiPartParser,)

    def get(self, request, format=None):
        instance = DocumentVersion.objects.all()
        serializer = DocumentVersionSerializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        print(request.FILES)
        return Response('nice')
