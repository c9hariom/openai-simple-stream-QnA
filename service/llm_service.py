from langchain_core.messages import HumanMessage

from core.config import Settings
from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self, model: str):
        self.llm = ChatOpenAI(
            model=model,
            base_url=Settings.OPENAI_ENDPOINT,
            api_key=Settings.OPENAI_API_KEY,
            streaming=True,
        )

    async def invoke(self, message: str):
        reply_chunk = []

        async for chunk in self.llm.astream([HumanMessage(content=message)]):
            content = getattr(chunk, "content", "")
            print(chunk)
            if content:
                print(content, end="", flush=True)
                reply_chunk.append(content)

        return "".join(reply_chunk)
