from api.auth import auth
from api.token import verify

from django.http import HttpResponseForbidden


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return HttpResponseForbidden("auth is required")

        if request.path == "/token/":
            user, error_message = auth(auth_header)

            if user:
                request.environ["user"] = user
                response = self.get_response(request)
                return response
            return HttpResponseForbidden(error_message)

        else:
            token = auth_header.replace("Bearer ", "")
            payload, error_message = verify(token)
            if payload:
                request.environ["username"] = payload["username"]
                request.environ["role"] = payload["role"]
                response = self.get_response(request)
                return response
            return HttpResponseForbidden(error_message)
