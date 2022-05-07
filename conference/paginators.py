from rest_framework.pagination import PageNumberPagination


class ConferencePagination(PageNumberPagination):
    page_size = 5
