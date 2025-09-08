import nltk
import random
from nltk.chat.util import Chat, reflections

# Pairs: user patterns and bot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am an AI chatbot built using NLTK.", "You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm doing great! How about you?", "I'm fine, thanks for asking!"]
    ],
    [
        r"what can you do?",
        ["I can answer simple questions and chat with you.", "I'm here to show how NLP chatbot works."]
    ],
    [
        r"(.*) project",
        ["I can help you with your internship project. Tell me more!", "Your project sounds interesting!"]
    ],
    [
        r"bye|goodbye|see you",
        ["Goodbye! Have a great day.", "See you later!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that.", "Can you rephrase?"]
    ]
]

def chatbot():
    print("Hi! I'm your AI Chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
