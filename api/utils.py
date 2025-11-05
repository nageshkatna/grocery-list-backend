from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class GroceryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"   # allow ?page_size=20
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "current_page": self.page.number,  # 👈 this is what you want
            "total_pages": self.page.paginator.num_pages,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })
