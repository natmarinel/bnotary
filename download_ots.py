import requests
import json


def download(url, ots):
 
    response = requests.get(url)
    
    try:
        
        open('./ots/'+ots, 'wb').write(response.content)
        print("Ots download e salavtaggio")

    except Exception as e:

        print("File non salvato")
        print(e)
          


