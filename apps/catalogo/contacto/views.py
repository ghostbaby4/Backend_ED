from drf_yasg.utils import swagger_auto_schema

from .models import Contacto

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ContactoSerializer


class ContactoAPIView(APIView):

    @swagger_auto_schema(responses={200: ContactoSerializer(many=True)})
    def get(self, request):
        serializer = ContactoSerializer(Contacto.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body= ContactoSerializer, responses={201: ContactoSerializer})
    def post(self, request):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactoDetails(APIView):
    @swagger_auto_schema(responses={200: ContactoSerializer})
    def get(self, request, pk=None):
        try:
            contacto = Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            return Response({'error': 'Contacto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContactoSerializer, responses={200: ContactoSerializer})
    def put(self, request, pk=None):
        try:
            contacto = Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            return Response({'error': 'Contacto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactoSerializer(contacto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ContactoSerializer, responses={200: ContactoSerializer})
    def patch(self, request, pk):
        try:
            contacto = Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            return Response({'error': 'Contacto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactoSerializer(contacto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204:'No contenido'})
    def delete(self, request, pk):
        try:
            contacto = Contacto.objects.get(pk=pk)
        except Contacto.DoesNotExist:
            return Response({'error': 'Contacto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        contacto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

