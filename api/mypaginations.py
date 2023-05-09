from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'             # http://127.0.0.1:8000/studentapi/?p=1
    page_size_query_param = 'records'  # http://127.0.0.1:8000/studentapi/?p=1&records=10
    max_page_size = 7                  # http://127.0.0.1:8000/studentapi/?p=7
    last_page_strings = ['end']        # http://127.0.0.1:8000/studentapi/?p=end