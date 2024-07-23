def audio(text, voiceid, lang):
    import requests
    import time
    code = 0

    for i in range(10):
        # Ensure text is a string
        if not isinstance(text, str):
            text = str(text)

        #get authkey from a file
        with open('elevenlabs.secret', 'r') as file:
            authkey = file.read().replace('\n', '')
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voiceid}"
        
        payload = {
            "text": text,
            "model_id": "eleven_turbo_v2_5",
            "language_code": lang
        }
        
        headers = { 
            "xi-api-key": authkey,
            "Content-Type": "application/json"
        }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        
        if response.status_code==200:
            return(response.content)
        elif i==0:
            print(response.status_code)
            print(response.text)
            time.sleep(1)