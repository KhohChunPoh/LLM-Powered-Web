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
    response = client.models.generate_content(
        model="gemma-4-31b-it", contents=prompt
        )

    return response.text

