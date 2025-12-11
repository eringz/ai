import requests, webbrowser
from playsound import playsound

def get_pronounciation(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    res = requests.get(url)
    
    if res.status_code != 200:
        print("Word not found")
        return
    
    data = res.json()[0]
    # print(f"Data: {data}")
    
    # print("WORD:", data["word"])
    # print("Phonetic:", data["phonetic"])
    # print(f"Phonetics: {data["phonetics"][0]["audio"]}")
    
    audio_url = data["phonetics"][0]["audio"]
    print(audio_url)
    webbrowser.open(audio_url)
    
    
    
    for p in data.get("phoenetics", []):
        if "text" in p:
            print("")


while True:
    word = input("Enter the word: ")
    get_pronounciation(word)