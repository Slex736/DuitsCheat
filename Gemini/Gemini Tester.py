from google import genai

# Initialize with your API key
client = genai.Client(api_key="AIzaSyBlRXQPTRimem1mwB1606Cy9BHM4_skdno")

# Use a model you actually have access to
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="what did diddy do?",
)

# Print safely
if hasattr(response, "text"):
    print(response.text)
elif hasattr(response, "content"):
    print(response.content)
else:
    print(response)
