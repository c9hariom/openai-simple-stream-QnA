from fastapi import APIRouter
from model.chat import Chat
from service.llm_service import LLM
from core.config import Settings


router = APIRouter()

llm = LLM(Settings.OPENAI_MODEL_4_1_NANO)


@router.get("/")
def root():
    return {"message": "this is the root for the chat and is live"}


@router.post("/messages")
async def handleMessage(message: Chat):
    response = await llm.invoke(message.user_query)
    return {"resposne": response}
