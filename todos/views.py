# todos/views.py
<<<<<<< HEAD
from rest_framework import status, viewsets
=======
from rest_framework import status, viewsets, generics
>>>>>>> fcba87d9aba674431dd54ea4b932190fa2b6c000
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, TodoSerializer
from .models import Todo
<<<<<<< HEAD
=======
from django.contrib.auth.models import User
>>>>>>> fcba87d9aba674431dd54ea4b932190fa2b6c000

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        result = Todo.objects.filter(user=self.request.user)
        return result
    
    def perform_create(self, serializer):
<<<<<<< HEAD
        serializer.save(user=self.request.user)
=======
        serializer.save(user=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
>>>>>>> fcba87d9aba674431dd54ea4b932190fa2b6c000
