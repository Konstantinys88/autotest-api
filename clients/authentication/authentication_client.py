import sys
import os

from public_http_builder import get_public_http_client
sys.path.append(os.path.join(os.path.dirname(__file__), 'clients'))
from clients.api_client import APIClient
from httpx import Response, Client
from typing import TypedDict


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str
    
class LoginResponseDict(TypedDict):
    token: Token

class LoginRequestDict(TypedDict):
    email: str
    password: str
    
class RefreshRequestDict(TypedDict):
    refreshToken: str 

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post('/api/v1/authentication/login', json=request)
    
    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post('/api/v1/authentication/refresh', json=request)
    
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()
    
def get_authentification_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
    
# base_url='http://localhost:8000'
# http_client = Client(base_url=base_url)
# client = AuthenticationClient(client=http_client)
# response = client.login_api({'email': 'user@example.com', 'password': 'string'})
# print(response.status_code)

