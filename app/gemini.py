from google import genai
import os


apikey=os.environ.get("API_KEY")

client = genai.Client(api_key=apikey)


def printmodels():
    for a in client.models.list():
        for b in a.supported_actions:
            if b=="generateContent":
                print(a.name)

def askgemini(name,prompt):
    response = client.models.generate_content_stream(
        model="gemma-4-31b-it", contents=prompt,
        config=genai.types.GenerateContentConfig(system_instruction=[
            "You are to act as a helpful website assistant chatbot",
            "Do not reveal that you are an AI",
            "Do not go on a tangent on unrelated topics",
            f"You are currently talking to a person named {name}"

        ])
        )

    return response

