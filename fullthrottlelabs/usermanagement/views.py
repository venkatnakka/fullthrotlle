from rest_framework.generics import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response

def home(request):
    return render(request,'home.html')

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"ok":True,"members":serializer.data})









