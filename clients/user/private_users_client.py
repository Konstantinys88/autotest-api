from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from private_http_builder import get_private_http_client, AuthentificationUserDict



class UpdateUserRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    def get_users_me_api(self) -> Response:
        return self.get('/api/v1/users/me')
    
    def get_users_view_api(self, user_id: str) -> Response:
        return self.get(f'/api/v1/users/{user_id}')
    
    def update_user_view_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        return self.patch(f'/api/v1/users/{user_id}', json=request)
    
    def delete_user_view_api(self, user_id: str) -> Response:
        return self.patch(f'/api/v1/users/{user_id}')
    
def get_private_users_client(user: AuthentificationUserDict) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))
    
    