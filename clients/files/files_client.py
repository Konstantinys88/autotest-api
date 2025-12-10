from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class DataFilesDict(TypedDict):
    filename: str
    directory: str
    upload_file: str
    

    

class FilesClient(APIClient):
    def get_files_api(self, file_id: str) -> Response:
        return self.get(f'/api/v1/files/{file_id}')
    
    def delete_files_api(self, file_id: str) -> Response:
        return self.delete(f'/api/v1/files/{file_id}')
    
    def post_file_api(self, request: DataFilesDict) -> Response:
        return self.post(
            '/api/v1/files', 
            data=request, 
            files={'upload_file': open(request['upload_file'], 'rb')}
            )