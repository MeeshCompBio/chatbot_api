from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class bot:
    def __init__(self) -> None:
        self.chatbot = ChatBot("Benoit")
        trainer = ListTrainer(self.chatbot)
        trainer.train(
            [
                "Hello",
                "Hello how are you",
                "I am doing well thanks" "So what do you like to do for fun?",
                "Code",
                "Oh really?, I have a great app idea if you want to hear it?",
                "No I dont",
                "What is your favorite type of keyboard",
                "Split",
                "Why is that?" "Because they are more ergonomic",
            ]
        )

    def bot_respose(self, msg):
        return self.chatbot.get_response(msg)
