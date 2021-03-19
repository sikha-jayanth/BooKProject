from django.shortcuts import render
from .serializers import BookSerializer,AuthorSerializer,AuthorDataSerializer
from .models import Books,Authors
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework import filters

# Create your views here.
# class AuthorCreateView(CreateAPIView):
#     serializer_class=AuthorDataSerializer
#     permission_classes=[IsAdminUser]
#     authentication_classes=[SessionAuthentication,BasicAuthentication]

class AuthorUpdateView(UpdateAPIView):
    serializer_class=AuthorDataSerializer
    permission_classes=[IsAdminUser]
    queryset=Authors.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]

class AuthorDetailView(RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorDataSerializer
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]





class BookCreateView(CreateAPIView):
    serializer_class=BookSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[SessionAuthentication,BasicAuthentication]

class BookListView(ListAPIView):
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]
    # search_fields = ['author','book_name','genre']
    search_fields = ['author_name__author_name','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset=Books.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]

class BookUpdateView(UpdateAPIView):
    serializer_class=BookSerializer
    permission_classes=[IsAdminUser]
    queryset=Books.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]

class BookDeleteView(DestroyAPIView):
    queryset = Books.objects.all()
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAdminUser]

class BookDetailView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAdminUser]

