import openai
import os
from dotenv import load_dotenv

# Load the API key from the .env file on the desktop
load_dotenv(r'C:\Users\karl4\Desktop\.env')

# Check if the API key is being loaded correctly
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Error: OPENAI_API_KEY not found in .env file!")
    exit(1)  # Exit if API key is not found
else:
    print("API Key loaded successfully")

# Set the API key in the openai package
openai.api_key = api_key

# Function to handle text completion
def generate_completion(prompt):
    try:
        # Request completion from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change this if you're using a different model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        # Get the generated text
        completion_text = response['choices'][0]['message']['content'].strip()

        # Output the generated text to the terminal
        print("\nGenerated Response:")
        print(completion_text)

    except Exception as e:
        print(f"Error: {e}")

# Main program execution
if __name__ == "__main__":
    # Get user input from the terminal
    prompt = input("Enter your prompt: ")

    # Call the function to generate completion
    generate_completion(prompt)
