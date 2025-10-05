import jwt
import datetime

from django.conf import settings


def epoch_time_in_one_hour() -> int:
    now = datetime.datetime.utcnow()
    one_hour_later = now + datetime.timedelta(hours=1)
    return int(one_hour_later.timestamp())


def int_now() -> int:
    now = datetime.datetime.utcnow()
    return int(now.timestamp())


def generate(user) -> str:
    secret = settings.SECRET_KEY
    return jwt.encode(
        {"username": user.username, "role": user.role, "exp": epoch_time_in_one_hour(), "iat": int_now()},
        secret,
        algorithm="HS256",
    )


def verify(token) -> (dict, str):
    secret = settings.SECRET_KEY
    payload = jwt.decode(token, secret, algorithms=["HS256"], options={
        "require": ["exp", "iat"],
        "verify_exp": "verify_signature"
    })
    return payload, None
