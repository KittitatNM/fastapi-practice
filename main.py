from fastapi import FastAPI
from schemas.user import ResponseMessage, UserLogin

app = FastAPI()

userLogin = [
    {
        "userId": 1,
        "userName": "name",
        "userPassword": "pass"
    }
]


@app.get('/')
async def root():
    return {'msg': 'Hello World'}


@app.get("/response", response_class=ResponseMessage)
def get_response():
    print(type(ResponseMessage(UserLogin)))
    print(ResponseMessage(UserLogin(userId=1, userName="test", userPassword="test")))
    pass
