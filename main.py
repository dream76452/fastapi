from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel,Field,EmailStr,ConfigDict
app=FastAPI()
data={
    "email":"abc@mail.com",
    "bio":"aaa",
    "age":12
}
data_wo_age={
    "email":"abc@mail.com",
    "bio":"aaa",
}
class UserSchema(BaseModel):
    email:EmailStr
    bio:str | None=Field(max_length=3)
    model_config=ConfigDict(extra="forbid")
users=[]
@app.get("/users")
def user()->list[UserSchema]:
    return users
@app.post("/users")
def add_user(user:UserSchema):
    users.append(user)
    return {"ok":True,"msg":"user append"}

class UserAgeShema(UserSchema):
    age:int = Field(ge=0,le=130)
user=UserAgeShema(**data)
user_2=UserSchema(**data_wo_age)
print(repr(user),f"\n{repr(user_2)}")
if __name__=="__main__":
    uvicorn.run("main:app",reload=True)