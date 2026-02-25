from pydantic import BaseModel

class Chat(BaseModel):
    user_query:str