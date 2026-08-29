import os
from dotenv import load_dotenv
from crew import generate_report

print(os.getenv("API_KEY"))
print(os.getenv("MODEL"))

topic = "Artificial Intelligence"

print("\nStarting Crew...\n")

result = generate_report(topic)

print("\n========== RESULT ==========\n")
print(result)