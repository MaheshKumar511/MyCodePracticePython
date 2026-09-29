from dataclasses import dataclass


@dataclass
class AuthResponse:
    token: str
    user_id: str
    message: str