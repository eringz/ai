import requests

def get_pronounciation(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    res = requests.get(url)
    
    if res.status_code != 200:
        print("Word not found")
        return
    
    data = res.json()[0]
    print(f"Data: {data}")
    
    # print("WORD:", data["word"])
    
    # for p in data.get("phoenetics", []):
    #     if "text" in p:
    #         print("")

get_pronounciation("computer")