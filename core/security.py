from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings
from django.http import HttpResponseForbidden

class BlockSuspiciousUserAgentsMiddleware:
    BLOCKED_AGENTS = ["sqlmap", "nmap", "nikto", "acunetix"]

    def __init__(self, get_response):
        self.get_response = get_response
        if settings.DEBUG:
            raise MiddlewareNotUsed  # devda ishlamasin

    def __call__(self, request):
        agent = request.META.get("HTTP_USER_AGENT", "").lower()
        if any(bad in agent for bad in self.BLOCKED_AGENTS):
            return HttpResponseForbidden("Blocked.")
        return self.get_response(request)