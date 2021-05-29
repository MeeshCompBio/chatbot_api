from fastapi.testclient import TestClient

from app import main
from bot_logic import bot

client = TestClient(main.app)


def test_empty_bot_response():
    mybot = bot.chat_bot()
    text = str(mybot.chat(""))
    assert text == "Send me some text to start the conversation"


def test_bot_response():
    mybot = bot.chat_bot()
    text = str(mybot.chat("Hello"))
    assert isinstance(text, str)


def test_chat_url():
    response = client.post("/chat/", json={"text": "Hello"})
    assert response.status_code == 200
    assert isinstance(response.json(), str)
