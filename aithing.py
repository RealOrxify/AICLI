import requests

# Function to perform the Grammarly API request
def grammarly_check(text):
    payload = {
        "text": text,
        "api_key": 'YOUR_GRAMMARLY_API_KEY'
    }

    response = requests.post('https://api.grammarbot.io/v2/check', json=payload)
    return response.json()

# Example usage
user_input = input("Enter text: ")
while user_input.lower() != "exit":
    response = grammarly_check(user_input)
    matches = response.get('matches', [])
    
    if matches:
        print("Grammar and writing suggestions:")
        for match in matches:
            print(f"- {match['message']['text']}")
    else:
        print("No suggestions found.")
    
    user_input = input("Enter text: ")
