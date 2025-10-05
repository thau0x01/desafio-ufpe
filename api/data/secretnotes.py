from api.codes.models import User, SecretNote
from rest_framework import serializers

class SecretNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretNote
        fields = ('id', 'note')


def get_user_secret_notes(username):
    if username:
        user = User.objects.get(username=username)
        notes = SecretNote.objects.filter(user=user)
        if len(notes) > 0:
            return SecretNoteSerializer(notes, many=True).data
        return f"{username} has no secrets"
    return []
