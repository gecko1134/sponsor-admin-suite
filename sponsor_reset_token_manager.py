import uuid
import json
import os
from datetime import datetime, timedelta

TOKEN_FILE = "reset_tokens.json"

def load_tokens():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return {}

def save_tokens(tokens):
    with open(TOKEN_FILE, "w") as f:
        json.dump(tokens, f, indent=2)

def generate_reset_token(email, expires_in_minutes=30):
    tokens = load_tokens()
    token = str(uuid.uuid4())
    expiration = (datetime.now() + timedelta(minutes=expires_in_minutes)).isoformat()
    tokens[token] = {"email": email, "expires": expiration}
    save_tokens(tokens)
    return token

def validate_token(token):
    tokens = load_tokens()
    if token in tokens:
        entry = tokens[token]
        if datetime.fromisoformat(entry["expires"]) > datetime.now():
            return entry["email"]
    return None

def expire_token(token):
    tokens = load_tokens()
    if token in tokens:
        del tokens[token]
        save_tokens(tokens)
