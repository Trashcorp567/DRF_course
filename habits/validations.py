from rest_framework import serializers


class HabitsValidator:

    def __init__(self, attr, attr_2, attr_3, attr_4):
        self.attr = attr
        self.attr_2 = attr_2
        self.attr_3 = attr_3
        self.attr_4 = attr_4

    def __call__(self, attrs):
        attr = attrs.get(self.attr)
        attr_2 = attrs.get(self.attr_2)
        attr_3 = attrs.get(self.attr_3)
        attr_4 = attrs.get(self.attr_4)

        if attr and attr_2:
            raise serializers.ValidationError(
                'Одновременный выбор связанной привычки и указания вознаграждения недопустим.')

        if attr_2 and (attr_3 or attr_4):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.')

        if not (attr_3 or attr_4):
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        if attr_4 > 120:
            raise serializers.ValidationError('Время выполнения не может быть больше 2 минут (120 секунд).')
