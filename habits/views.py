from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitsListPaginator
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner, Admin


class CreateHabitsAPIView(generics.CreateAPIView):
    """Контроллер создания привычки"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Добавление пользователя в поле владельца"""
        serializer.save(owner=self.request.user, is_public=True)
        return super().perform_create(serializer)


class ListHabitsAPIView(generics.ListAPIView):
    """Просмотр списка своих привычек"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, Admin]
    pagination_class = HabitsListPaginator


class FullListHabitsAPIView(generics.ListAPIView):
    """Просмотр списка всех привычек"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsListPaginator

    def get_queryset(self):
        """Фильтрация вывода по статусу"""
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)


class UpdateHabitsAPIView(generics.UpdateAPIView):
    """Обновление привычки"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, Admin]


class RetrieveHabitsAPIView(generics.RetrieveAPIView):
    """Просмотр одного объекта"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, Admin]


class DestroyHabitsAPIView(generics.DestroyAPIView):
    """Контроллер удаления привычки"""
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, Admin]