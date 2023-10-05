import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the GPT-3.5 Chatting System!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'exit':
            break
        
        # Send user input as prompt to GPT-3.5
        response = chat_with_gpt3(user_input)
        
        print("GPT-3.5: " + response)

if __name__ == "__main__":
    main()