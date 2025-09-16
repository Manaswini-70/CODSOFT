def respond(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I am fine, thank you! How are you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

def chat():
    print("Chatbot is ready. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = respond(user_input)
        print("Bot:", response)
        if user_input.lower() == "bye":
            break

chat()
