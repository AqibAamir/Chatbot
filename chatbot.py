def chatbot():
    print("Hello! I'm your friendly chatbot. How can I help you today?")
    print("You can ask me about various topics including food, hobbies, education, technology, religion, and more. Type 'bye' to exit the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "weather" in user_input:
            print("Chatbot: It's typically cloudy in the UK, but it's always good to check the local forecast.")
        elif "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif "quote" in user_input:
            print("Chatbot: 'The only way to do great work is to love what you do.' - Steve Jobs")
        elif "fact" in user_input:
            print("Chatbot: Did you know that honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.")
        elif "movie" in user_input:
            print("Chatbot: I recommend watching 'Inception' for a mind-bending experience or 'The Lion King' for a classic adventure.")
        elif "hobby" in user_input:
            print("Chatbot: Coding is a fantastic hobby! You could also try something creative like painting or playing an instrument.")
        elif "food" in user_input:
            print("Chatbot: Pizza is always a great choice! What's your favorite topping?")
        elif "music" in user_input:
            print("Chatbot: How about some classic rock? The Beatles and Queen are timeless favorites.")
        elif "exercise" in user_input:
            print("Chatbot: Regular exercise is important. You could go for a run, do some yoga, or even just take a brisk walk.")
        elif "book" in user_input:
            print("Chatbot: If you love fantasy, you should read 'The Hobbit' by J.R.R. Tolkien. For something more contemporary, try 'The Alchemist' by Paulo Coelho.")
        elif "travel" in user_input:
            print("Chatbot: Traveling is amazing! Have you considered visiting Japan? It's a beautiful country with a rich culture and stunning landscapes.")
        elif "technology" in user_input:
            print("Chatbot: Technology is evolving rapidly. Did you hear about the latest advancements in AI? It's fascinating how it's changing our world.")
        elif "history" in user_input:
