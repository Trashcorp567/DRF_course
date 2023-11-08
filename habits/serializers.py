from rest_framework import serializers
from habits.models import Habit
from habits.validations import HabitsValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitsValidator(attr='reward', attr_2='pleasant_habit',
                                     attr_3='is_pleasant', attr_4='time_to_complete')]
