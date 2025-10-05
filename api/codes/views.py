from django.http import HttpResponseForbidden

from rest_framework.views import APIView
from rest_framework.response import Response


from api.token import generate
from api.data.protected import get_codes
from api.data.secretnotes import get_user_secret_notes, SecretNoteSerializer


class TokenView(APIView):
    def get(self, request):
        user = request.environ["user"]
        token = generate(user)
        content = {"access": token}
        return Response(content)


class ImportantView(APIView):
    def get(self, request):
        role = request.environ["role"]
        if role:
            codes = get_codes(role)
            return Response(codes)
        
        return HttpResponseForbidden()


class SecretNotestView(APIView): 
    def get(self, request):
        secret_notes = get_user_secret_notes(request.environ["username"])
        return Response({"secret_notes": secret_notes})
