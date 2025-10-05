
from api.codes.models import User

def get_user(username):
    user = User.objects.get(username=username)
    return user
