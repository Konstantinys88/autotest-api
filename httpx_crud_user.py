import httpx
from tools.fakers import get_random_email

# Создать пользователя
user_payload = {
  "email": get_random_email(),
  "password": "admin",
  "lastName": "Oleg",
  "firstName": "Semen",
  "middleName": "Egor"
}
response = httpx.post('http://localhost:8000/api/v1/users', json=user_payload)
user_payload_dara = response.json()
print(f'Status: {response.status_code}, Response: {user_payload_dara}')

# Аутентификация
login_payload = {
    "email": f'{user_payload_dara['user']['email']}',
    "password": "admin"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f'Status: {login_response.status_code}, Login response: {login_response_data}')

# Получение пользователя
user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
user_id = user_payload_dara['user']['id']
# print(user_id)
response = httpx.get(f'http://localhost:8000/api/v1/users/{user_id}', headers=user_headers)
user_id_data = response.json()
print(f'Status: {response.status_code}, Response: {user_id_data}')


patch_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
response = httpx.patch(f'http://localhost:8000/api/v1/users/{user_id}', json=patch_user_payload, headers=user_headers)
patch_user_data = response.json()
print(f'Status: {response.status_code}, Response: {patch_user_data}')

# удаление пользователя
response = httpx.delete(f'http://localhost:8000/api/v1/users/{user_id}', headers=user_headers)
delete_respons_data = response.json()
print(f'Status: {response.status_code}, Response: {delete_respons_data}')

# Получение пользователя
user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
user_id = user_payload_dara['user']['id']
# print(user_id)
response = httpx.get(f'http://localhost:8000/api/v1/users/{user_id}', headers=user_headers)
user_id_data = response.json()
print(f'Status: {response.status_code}, Response: {user_id_data}')