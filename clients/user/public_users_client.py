import sys
import os

from public_http_builder import get_public_http_client
sys.path.append(os.path.join(os.path.dirname(__file__), 'clients'))
from clients.api_client import APIClient
from httpx import Response, Client
from typing import TypedDict

base_url='http://localhost:8000'

class UserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self, request: UserRequestDict) -> Response:
        return self.post('/api/v1/users', json=request)
    
    
def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())
    
# Создаем HTTP-клиент
# http_client = Client(base_url=base_url)

# Создаем экземпляр публичного клиента, передавая HTTP-клиент
# client = PublicUsersClient(client=http_client)

# Запрашиваем создание пользователя
# response = client.create_user_api({
#     "email": "test4345@example.com",
#     "password": "secure_password",
#     "lastName": "Иванов",
#     "firstName": "Иван",
#     "middleName": "Иванович"
# })

# Проверяем статус ответа
# respons_data = response.json()
# print(f'Status: {response.status_code}, Data: {respons_data}')