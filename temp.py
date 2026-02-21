import requests

apikey = "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"
word=input("enter your word:")

res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

print("status code:",res.status_code)
if res.status_code == 200:
    
    meanings = res.json()[0]["meanings"]
    for meaning in meanings:
        defn = meaning["definitions"]
        for d in defn:
            print(d['definition'])
else:
    print("word not found in dictionary")               
    
