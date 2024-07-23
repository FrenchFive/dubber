def audio(text, voiceid):
    import requests

    # Ensure text is a string
    if not isinstance(text, str):
        text = str(text)

    #get authkey from a file
    with open('elevenlabs.secret', 'r') as file:
        authkey = file.read().replace('\n', '')
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voiceid}"
    
    payload = {
        "text": text,
    }
    
    headers = { 
        "xi-api-key": authkey,
        "Content-Type": "application/json"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    if response.status_code==200:
        return(response.content)
    else:
        print(response.status_code)
        print(response.text)