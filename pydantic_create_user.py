from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError

class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    
    
class CreateUserRequestSchema(BaseModel):
    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    
class CreateUserResponseSchema(BaseModel):
   user: UserSchema       