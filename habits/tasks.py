import os
import requests
from celery import shared_task
from rest_framework import response

from habits.models import Habit


def reward_or_habit():
    habits = Habit.objects.all()
    for habit in habits:
        reward = habit.reward
        pleasant = habit.pleasant_habit
        if reward:
            habit = reward
        else:
            habit = pleasant
        return habit


@shared_task
def habit_bot():
    send_habit = Habit.objects.all()
    for h in send_habit:
        action = h.habit_action
        time = h.time
        place = h.place
        text = f'Я должнен {action} в {time} в {place}'
        params = {"chat_id": os.getenv('CHANNEL_ID'), 'text': text}
        requests.get(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage", params=params)
