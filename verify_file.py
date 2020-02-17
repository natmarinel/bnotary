import requests
import json
import download_ots
import delete_tmp_file
import time

def verify(hash, otsFilename, timestamp):
    
    #hash = '5e440ea1c80d0d17ac51ccd9a256aec35a469d3d60d19b08e929087e2f0a6151'
    #otsFilename = '12.txt.ots'
    #timestamp = '154321'
    print(hash)
    print(type(hash))
    print(otsFilename)
    print(type(otsFilename))
    url = 'https://notaryb-api.bcademy.it/api/v1/verify/file'
    apiKey = 'fcee94e161c3db5b0e8014f75c34b6c4c02ac415a7e2fe7057e4f0e0146cac77'
    headers = {'Content-Type': 'application/json', 'apiKey': apiKey}
    a = {'hash': hash, 'otsFilename': otsFilename, 'timestamp': timestamp}

    response = requests.post(url, headers=headers, json=a)
    print(type(response))
    
    print(response.status_code)
    print(response.json())
    print("\nStato Verifica: ", response.json()['verifyStatus'])
    
    status = response.json()['verifyStatus']
    
    while  status != 'verified':
    
        response = requests.post(url, headers=headers, json=a)
        status = response.json()['verifyStatus']

        if status == 'verified':
      
            urlOts = response.json()['file']
            download_ots.download(urlOts, otsFilename)
            print(otsFilename, " Verified")
            delete_tmp_file.delete()
            print("All file deleted")
        
        print( otsFilename + " non verificato")
        time.sleep(1800)


