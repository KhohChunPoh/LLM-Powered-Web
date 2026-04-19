from google import genai


keyfile=open("key.txt",'r')
apikey=keyfile.readline()
keyfile.close()

client = genai.Client(api_key=apikey)


def printmodels():
    for a in client.models.list():
        for b in a.supported_actions:
            if b=="generateContent":
                print(a.name)

def askgemini(prompt):
    response = client.models.generate_content_stream(
        model="gemma-4-31b-it", contents=prompt,
        config=genai.types.GenerateContentConfig(system_instruction=[
            "You are to act as a helpful website assistant chatbot",
            "Do not reveal that you are an AI",
            "Do not go on a tangent on unrelated topics",

        ])
        )

    return response

