from rest_framework import status
from rest_framework.test import APITestCase


from habits.models import Habit
from habits.validations import HabitsValidator
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Test',
            password='123qwe456rty'
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_status(self):
        """Тест создания привычки"""
        data = {
            "place": "Дома",
            "time": "16:44:22",
            "habit_action": "Встать со стула",
            "time_to_complete": 10
        }
        response = self.client.post(
            'http://localhost:8000/habits/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_habits_validation_max_time(self):
        """Тест валидации времени на выполнение"""
        data = {
            "place": "Дома",
            "time": "16:44:22",
            "habit_action": "Встать со стула",
            "time_to_complete": 130
        }

        response = self.client.post(
            'http://localhost:8000/habits/create/',
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Время выполнения не может быть больше 2 минут (120 секунд).']})

    def test_habits_validation_connection(self):
        """Тест валидации связей"""
        habit = Habit.objects.create(
                place="Дома",
                time="16:44:22",
                habit_action="Встать со стула",
                time_to_complete=120,
                is_pleasant=True
        )
        data = {
            "place": "Дома",
            "time": "16:44:22",
            "habit_action": "Встать со стула",
            "time_to_complete": 120,
            "pleasant_habit": habit.id,
            "reward": "Выпить светлое нефильтрованное",
        }
        data2 = {
            "place": "Дома",
            "time": "16:44:22",
            "habit_action": "Встать со стула",
            "time_to_complete": 120,
            "pleasant_habit": habit.id,
            "is_pleasant": True,
        }
        response = self.client.post(
            'http://localhost:8000/habits/create/',
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': [
                             'Одновременный выбор связанной привычки и указания вознаграждения недопустим.'
                         ]})
        response2 = self.client.post(
            'http://localhost:8000/habits/create/',
            data=data2
        )
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.json(),
                         {'non_field_errors': [
                             'У приятной привычки не может быть вознаграждения или связанной привычки.'
                         ]})
