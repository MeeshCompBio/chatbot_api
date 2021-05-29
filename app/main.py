from fastapi import FastAPI
from pydantic import BaseModel

from bot_logic import bot

app = FastAPI()
api_bot = bot.chat_bot()


class Message(BaseModel):
    text: str


@app.post("/chat/")
async def chat_bot(msg: Message):
    return str(api_bot.chat(msg.text))
