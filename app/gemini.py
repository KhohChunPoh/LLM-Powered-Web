from google import genai
import os


apikey=os.environ.get("API_KEY")

client = genai.Client(api_key=apikey)

class errorresponse:
    text="Assistant is busy, try again in a minute."


def printmodels():
    for a in client.models.list():
        for b in a.supported_actions:
            if b=="generateContent":
                print(a.name)

def askgemini(name,prompt):
    try:
        response = client.models.generate_content_stream(
            model="gemma-4-31b-it", contents=prompt,
            config=genai.types.GenerateContentConfig(system_instruction=[
                "You are to act as a helpful assistant chatbot, but be absolutely based",
                "Do not reveal that you are an AI",
                "Do not go on a tangent on unrelated topics",
                f"You are currently talking to a person named {name}, just keep that in mind, no need to explicitly mention it",

            ])
            )
        for a in response:
            yield a

    except:
        yield errorresponse
