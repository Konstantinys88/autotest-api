# uvicorn main:app --reload
# Теперь сервер будет запущен локально на вашем компьютере и доступен по адресу http://localhost:8000. 
# Чтобы открыть документацию к доступным эндпоинтам, перейдите по адресу http://localhost:8000/docs. 
# Здесь вы найдете Swagger документацию, где будут перечислены все доступные методы взаимодействия с сервером.

import httpx

login_payload = {
  "email": "test@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f'Status: {login_response.status_code}, Login response: {login_response_data}')


refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()

print(f'Status: {refresh_response.status_code}, Login response: {refresh_response_data}')

