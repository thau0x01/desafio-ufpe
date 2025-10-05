import base64
import bcrypt

from .data import users


def auth(auth_header) -> (str, str):

    method = auth_header.split(" ")[0]

    if method == "Basic":
        encoded = auth_header.replace("Basic ", "")
        data_bytes = base64.b64decode(encoded)
        data = data_bytes.decode("utf-8")
        credentials = data.split(":")
        username = credentials[0]
        password = credentials[1]
        password = password.encode("utf-8")

        user = users.get_user(username)

        if user:
            if bcrypt.checkpw(password=password, hashed_password=user.password.encode("utf-8")):
                return user, None
            else:
                error_message = f"Wrong password for {username}"
                print(error_message)
                return None, error_message
        else:
            return None, f"{username} not found."
    else:
        return None, "Invalid method"
