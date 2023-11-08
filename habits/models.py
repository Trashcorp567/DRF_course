from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    PERIOD = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'каждую неделю')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время', default='08:00:00')
    habit_action = models.TextField(verbose_name='действие')
    pleasant_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', default=False)
    period = models.CharField(max_length=15, verbose_name='Периодичность', choices=PERIOD, default='DAILY')
    time_to_complete = models.PositiveIntegerField(default=120, verbose_name='Время на выполнение в секундах')
    reward = models.TextField(verbose_name='Награда', **NULLABLE)
    is_public = models.BooleanField(verbose_name='Признак публичности', default=False)

    def __str__(self):
        return f"Привычка: {self.habit_action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
