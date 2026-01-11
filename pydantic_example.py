from pydantic import BaseModel

class AddressSchema(BaseModel):
    city: str
    zip_code: str

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool 
    
user = UserSchema(
    id=2, 
    name="Egor", 
    email="egor@example,com",
    is_active=True
)

print(user.model_dump_json())