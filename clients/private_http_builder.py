from httpx import Client
from authentication.authentication_client import get_authentification_client, LoginRequestDict
from typing import TypedDict

class AuthentificationUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthentificationUserDict) -> Client:
    authentification_client = get_authentification_client()
    login_request = LoginRequestDict(email=user['email'],password=user['password'])
    login_response = authentification_client(login_request)
    
    
    return Client(
        timeout=100, 
        base_url="http://localhost:8000", 
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
        )