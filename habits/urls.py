from django.urls import path
from habits.apps import HabitsConfig
from habits.views import CreateHabitsAPIView, UpdateHabitsAPIView, RetrieveHabitsAPIView, ListHabitsAPIView, \
    FullListHabitsAPIView, DestroyHabitsAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', CreateHabitsAPIView.as_view(), name='create_habit'),
    path('update/', UpdateHabitsAPIView.as_view(), name='update_habit'),
    path('view/<int:pk>/', RetrieveHabitsAPIView.as_view(), name='view_habit'),
    path('mylist/', ListHabitsAPIView.as_view(), name='my_habits_list'),
    path('fulllist/', FullListHabitsAPIView.as_view(), name='full_list_of_habits'),
    path('delete/', DestroyHabitsAPIView.as_view(), name='delete_habit'),
]