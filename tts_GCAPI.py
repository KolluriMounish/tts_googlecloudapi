import requests
import base64

API_KEY = "YOUR_API_KEY"  # paste your key here

def telugu_tts(text, output_file="output.mp3"):
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"
    
    payload = {
        "input": {"text": text},
        "voice": {
            "languageCode": "te-IN",
            "name": "te-IN-Chirp3-HD-Zephyr",   # ✅ capital W, lowercase n
            "ssmlGender": "FEMALE"
        },
        "audioConfig": {"audioEncoding": "MP3"}
    }
    
    response = requests.post(url, json=payload)
    data = response.json()
    
    if "audioContent" in data:
        audio_data = base64.b64decode(data["audioContent"])
        with open(output_file, "wb") as f:
            f.write(audio_data)
        print(f"✅ Audio saved to {output_file}")
    else:
        print("❌ Error:", data)

telugu_tts("నమస్కారం! ఇది తెలుగు వాయిస్ టెస్ట్.")


# ------------------------ #To get available voice names ----------------------------------
# # import requests

# # API_KEY = "YOUR_API_KEY"  # paste your key here

# url = f"https://texttospeech.googleapis.com/v1/voices?key={API_KEY}&languageCode=te-IN"
# response = requests.get(url)
# data = response.json()

# print("Available Telugu Voices:")
# for voice in data.get("voices", []):
#     print(f"  Name: {voice['name']} | Gender: {voice['ssmlGender']}")
