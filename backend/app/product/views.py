from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Flower, Bunch
from .serializers import FlowerSerializer, BunchSerializer


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class BunchViewSet(viewsets.ModelViewSet):
    queryset = Bunch.objects.all()
    serializer_class = BunchSerializer


# class FlowerView(APIView):
    # def get(self, request):
    #     flowers = Flower.objects.all()
    #     serializer = FlowerSerializer(flowers, many=True)
    #     return Response({"flowers": serializer.data})

    # def get(self, request, pk=None):
    #     if pk:
    #         flowers = [get_object_or_404(Flower.objects.all(), pk=pk)]
    #     else:
    #         flowers = Flower.objects.all()
    #     serializer = FlowerSerializer(flowers, many=True)
    #     return Response({"flowers": serializer.data})

#     def post(self, request):
#         flower = Flower(name=request.data.get('name'))
#         if request.data.get('color'):
#             flower.color = request.data.get('color')
#         flower.save()
#         return Response(status=201)
#
#     def put(self, request, pk):
#         flower = get_object_or_404(Flower.objects.all(), pk=pk)
#
#         if request.data.get('name'):
#             flower.color = request.data.get('name')
#
#         if request.data.get('color'):
#             flower.color = request.data.get('color')
#         flower.save()
#         return Response(status=201)
#
#     def delete(self, request, pk):
#         flower = get_object_or_404(Flower.objects.all(), pk=pk)
#         flower.delete()
#         return Response(status=204)
#
#
# class BunchView(APIView):
#     def get(self, request):
#         bunch = Bunch.objects.all()
#         serializer = BunchSerializer(bunch, many=True)
#         return Response({"bunch": serializer.data})
#
#     def post(self, request):
#         bunch = Bunch(name=request.data.get('name'))
#         # if request.data.get('color'):
#         #     bunch.color = request.data.get('color')
#         bunch.save()
#         return Response(status=201)
#
#     def delete(self, request, pk):
#         bunch = get_object_or_404(Bunch.objects.all(), pk=pk)
#         bunch.delete()
#         return Response(status=204)
