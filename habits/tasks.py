import os
import requests
from celery import shared_task
from rest_framework import response

from habits.models import Habit

habits = Habit.objects.all()
for f in habits:
    action = f.habit_action
    time = f.time
    place = f.place
    reward = f.reward
    pleasant = f.pleasant_habit


def reward_or_habit():
    if reward:
        habit = reward
    else:
        habit = pleasant
    return habit


@shared_task
def habits_bot():
    chat_id = "5378117630"
    text = f'Я должен {action} в {time} в {place}' '\n'
    f'А после{reward_or_habit()}'
    params = {"chat_id": chat_id, 'text': text}
    requests.post(f"https://api.telegram.org/bot{os.getenv('TG_BOT')}/sendMessage", params=params)
    if response:
        print(f"Сообщение успешно отправлено пользователю {chat_id}")
    else:
        print(f"Не удалось отправить сообщение. Код статуса: {response.json()}")
habits_bot.delay()