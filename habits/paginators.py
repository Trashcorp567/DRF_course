from rest_framework.pagination import PageNumberPagination


class HabitsListPaginator(PageNumberPagination):
    page_size = 5
