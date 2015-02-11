class MultipleProxyMiddleware(object):
    FORWARDED_FOR_FIELDS = [
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_FORWARDED_HOST',
        'HTTP_X_FORWARDED_SERVER',
    ]

    TRUST_PROXIES = [
        '127.0.0.1',
    ]

    def process_request(self, request):
        """
        Rewrites the proxy headers so that only the most
        recent proxy is used.
        """
        for field in self.FORWARDED_FOR_FIELDS:
            if field in request.META and ',' in request.META[field]:
               parts = request.META[field].split(',')
               for part in parts[::-1]:
                   part = part.strip()
                   if part not in self.TRUST_PROXIES:
                       request.META[field] = part
                       break
