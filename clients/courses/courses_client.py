from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from private_http_builder import AuthentificationUserDict, get_private_http_client

class RequestCreateCourseViewDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str
    
class RequestUpdateCourseViewDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    
    def get_courses_view_api(self, query: str) -> Response:
        return self.get(f'/api/v1/courses', params=query)
    
    def post_create_course_view_api(self, request: RequestCreateCourseViewDict) -> Response:
        return self.post(f'/api/v1/courses', json=request)
    
    def get_courses_view_course_id_api(self, course_id: str) -> Response:
        return self.get(f'/api/v1/courses/{course_id}')
    
    def patch_update_course_view_api(self, course_id: str, request: RequestUpdateCourseViewDict) -> Response:
        return self.patch(f'/api/v1/courses/{course_id}', json=request)
    
    def delete_courses_view_api(self, course_id: str) -> Response:
        return self.get(f'/api/v1/courses/{course_id}')
    
    
def get_courses_client(user: AuthentificationUserDict) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))