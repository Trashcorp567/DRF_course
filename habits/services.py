from django_celery_beat.models import IntervalSchedule

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