from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Gemini API key missing!")
    print("Check your .env file.")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

print("=" * 50)
print("       GEMINI AI CHATBOT")
print("=" * 50)
print("Ask me anything!")
print("Type 'exit' to stop the chatbot.")
print()

while True:

    # Take question from user
    question = input("You: ")

    # Exit condition
    if question.lower() == "exit":
        print("Gemini: Goodbye! 👋")
        break

    # Don't send empty questions
    if not question.strip():
        print("Gemini: Please enter a question.")
        continue

    try:
        # Send question to Gemini
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=question
        )

        # Display answer
        print("\nGemini:", response.text)
        print()

    except Exception as e:
        print("\n❌ Error:", e)
        print()