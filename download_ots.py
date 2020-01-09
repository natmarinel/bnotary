#script to download ots files from api bnotary when file's verifyStatus is verified
#use request get to download the files
#when the file is downloaded, it is stored inside directory ./ots 
import requests
import json


def download(url, ots):
    
    print(url)
    response = requests.get(url)
    
    try:
        
        open('./ots/'+ots, 'wb').write(response.content)
        print("Ots download e salavtaggio")

    except Exception as e:

        print("File non salvato")
        print(e)
          


