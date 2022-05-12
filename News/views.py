from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend



class NewsViewSet(viewsets.ModelViewSet):
    # queryset = News.objects.all()
    # serializer_class = NewsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return News.objects.all()

        return News.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return NewsWriteSerializer

        return NewsReadSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ["news_type"]
    # search_fields = ['news_type']


    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:

    #         return News.objects.all()[:3]

    #     serializer_class = NewsSerializer2
    #     return News.objects.filter(pk=pk)

    # @action(methods=["get"], detail=True)
    # def newstype(self, request, pk=None):
    #     types = NewsType.objects.get(pk=pk)
    #     return Response({"type": types.name, "color": types.color})

    # @action(methods=["get"], detail=False)
    # def newstypes(self, request):
    #     types = NewsType.objects.all()
    #     return Response([{"name": t.name, "color": t.color} for t in types])

class NewsTypeViewSet(viewsets.ModelViewSet):
    queryset = NewsType.objects.all()
    serializer_class = NewsTypeSerializer



# class NewsAPIList(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsAPIUpdate(generics.UpdateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsAPIDEtailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


# class NewsTypeAPIList(generics.ListCreateAPIView):
#     queryset = NewsType.objects.all()
#     serializer_class = NewsTypeSerializer

# class NewsTypeAPIUpdate(generics.UpdateAPIView):
#     queryset = NewsType.objects.all()
#     serializer_class = NewsTypeSerializer

# class NewsTypeAPIDEtailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = NewsType.objects.all()
#     serializer_class = NewsTypeSerializer