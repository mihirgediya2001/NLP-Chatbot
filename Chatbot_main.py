import Chatbot_Controller
from Chatbot_Responses import responses 

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Goodbye! Have a great day!")
            break
        response = Chatbot_Controller.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()

