from rest_framework import pagination
from rest_framework.response import Response


class BasePagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        self.count = queryset.count()
        try:
            self.available_products_count = queryset.filter(warehouse_status='avl').count()
        except:
            self.available_products_count = None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.num_pages,
            'count_all': self.count,
            'available_products_count': self.available_products_count,
            'results': data
        })
