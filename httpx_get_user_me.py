import httpx

login_payload = {
  "email": "test@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f'Status: {login_response.status_code}, Login response: {login_response_data}')

user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=user_headers)
user_response_data = user_response.json()
print(f'Status: {user_response.status_code}, Login response: {user_response_data}')