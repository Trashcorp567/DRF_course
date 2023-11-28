import json

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habit


def schedule():
    habit = Habit.object.all()
    if habit.PERIOD == "DAILY":
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )
        return schedule
    else:
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=7,
            period=IntervalSchedule.DAYS,
        )
        return schedule


def create_schedule():
    habit = Habit.objects.all()
    for h in habit:
        time = h.time
        PeriodicTask.objects.create(
            interval=schedule(),
            name='Habit reminder',
            task='habit.tasks.habit_bot',
            args=json.dumps(['arg1', 'arg2']),
            kwargs=json.dumps({'arg1': 'arg2'}),
            crontab=time,
        )