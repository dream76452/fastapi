from pydantic import BaseModel,Field,EmailStr
data={
    "email":"abc@mail.com",
    "bio":"aaa",
    "age":12
}
data_wo_age={
    "email":"abc@mail.com",
    "bio":"aaa"
}
class UserSchema(BaseModel):
    email:EmailStr
    bio:str | None=Field(max_length=3)
class UserAgeShema(UserSchema):
    age:int = Field(ge=0,le=130)
user=UserAgeShema(**data)
user_2=UserSchema(**data_wo_age)
print(repr(user),f"\n{repr(user_2)}")