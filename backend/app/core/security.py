def verify_credentials(username: str, password: str):
    # Minimal — in-memory fake login
    return username == "admin" and password == "admin123"
