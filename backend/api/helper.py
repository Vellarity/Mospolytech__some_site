from rest_framework import pagination
from rest_framework.response import Response
import math

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        first_page = 1
        last_page = self.page.paginator.num_pages 

        iter_pages = get_displayed_page_numbers(self.page.number, last_page)

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'first_page':first_page,
            'last_page':last_page,
            'this_page':self.page.number,
            'iter_pages':iter_pages,
            'count': self.page.paginator.count,
            'results': data
        })
    
def get_displayed_page_numbers(current, final):
    """
    This utility function determines a list of page numbers to display, based
    on the same pagination display style that GitHub use in their issue list pages.
    This gives us a nice contextually relevant set of page numbers to display.
    For example:
    current=14, final=16 -> [1, 2, None, 12, 13, 14, 15, 16]
    current=2, final=16 -> [1, 2, 3, 4, 5, None, 15, 16]
    current=8, final=16 -> [1, 2, None, 6, 7, 8, 9, 10, None, 15, 16]
    """
    assert current >= 1
    assert final >= current

    if final <= 8:
        return [i for i in range(1, final + 1)]

    # We always include the first two pages, last two pages, and
    # two pages either side of the current page.
    included = set((
        1, 2,
        current - 2, current - 1, current, current + 1, current + 2,
        final - 1, final
    ))

    # At the edges we include more page numbers.
    if current <= 6:
        included.add(3)
        included.add(4)
        included.add(5)
    if current >= final - 5:
        included.add(final - 2)
        included.add(final - 3)
        included.add(final - 4)

    # Now sort the page numbers and drop anything outside the limits.
    included = [
        idx for idx in sorted(list(included))
        if idx > 0 and idx <= final
    ]

    # Finally insert any `...` breaks
    if current > 6:
        included.insert(2, None)
    if current < final - 5:
        included.insert(len(included) - 2, None)
    return included