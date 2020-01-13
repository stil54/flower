from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Flower
from .serializers import FlowerSerializer


class FlowerView(APIView):
    def get(self, request):
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response({"flowers": serializer.data})

    def get(self, request, pk):
        flower = get_object_or_404(Flower.objects.all(), pk=pk)

        serializer = FlowerSerializer([flower], many=True)
        return Response({"flower": serializer.data})

    def post(self, request):
        flower = Flower(name=request.data.get('name'))
        if request.data.get('color'):
            flower.color = request.data.get('color')
        flower.save()
        return Response(status=201)

    def put(self, request, pk):
        flower = get_object_or_404(Flower.objects.all(), pk=pk)

        if request.data.get('name'):
            flower.color = request.data.get('name')

        if request.data.get('color'):
            flower.color = request.data.get('color')
        flower.save()
        return Response(status=201)

    def delete(self, request, pk):
        flower = get_object_or_404(Flower.objects.all(), pk=pk)
        flower.delete()
        return Response(status=204)
