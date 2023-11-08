from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from users.models import User
from users.serializers import UserSerializer


class UserCreationApiView(generics.CreateAPIView):
    """Создание пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Хеширование пароля """
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password
        return super().create(request, *args, **kwargs)


class UserListApiView(generics.ListAPIView):
    """Просмотр всех пользователей (только для пользователей со статусом superuser)"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
