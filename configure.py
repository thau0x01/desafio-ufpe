import os
import random
import string
import shutil

# Generate a random key
def generate_key():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(64))

# .env files path
env_path = ".env"
env_example_path = ".env.example"

# if .env file does not exists, then copy .env.example file to .env 
if not os.path.isfile(env_path):
    shutil.copyfile(env_example_path, env_path)

secret_key_updated = False
# Update SECRET_KEY value in the .env file
lines = []
with open(env_path, "r") as f:
    lines = f.readlines()

with open(env_path, "w") as f:
    key = generate_key()
    for line in lines:
        if line.startswith("SECRET_KEY="):
            f.write(f"SECRET_KEY=\"{key}\"\n")
            secret_key_updated = True
        else:
            f.write(line)

# Define a chave como variável de ambiente
if secret_key_updated:
    os.environ["SECRET_KEY"] = key

print("SECRET_KEY successfuly created!")
