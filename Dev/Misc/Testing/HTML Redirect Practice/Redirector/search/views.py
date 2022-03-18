# search.views.py
from django.views.generic.base import RedirectView

class SearchRedirectView(RedirectView):
    url = "https://google.com/?q=%(term)s"

class RandomSearchView(RedirectView):
    search_urls = [
        "https://google.com/?q=%(term)s",
        "https://duckduckgo.com/?q=%(term)s",
        "https://www.bing.com/search?q=%(term)s",
    ]

    def get_redirect_url(self, *args, **kwargs):
        from random import choice
        return choice(self.search_urls) % kwargs
