import requests
import json
import download_ots
import delete_tmp_file
import time

def verify(hash, otsFilename, timestamp):

    #hash = '5e440ea1c80d0d17ac51ccd9a256aec35a469d3d60d19b08e929087e2f0a6151'
    #otsFilename = '12.txt.ots'
    print(hash)
    print(type(hash))
    print(otsFilename)
    print(type(otsFilename))
    url = 'http://localhost:5001/api/v1/verify/file'
    apiKey = '3581ca332d59abbbb665c6ec993642ab8c576b06e95e7a916e06edd6fd9b49ba'
    headers = {'Content-Type': 'application/json', 'apiKey': apiKey}
    a = {'hash': hash, 'otsFilename': otsFilename, 'timestamp': timestamp}

    response = requests.post(url, headers=headers, json=a)
    print(type(response))
    
    print(response.status_code)
    print(response.json())
    print("\nStato Verifica: ", response.json()['verifyStatus'])
    
    status = response.json()['verifyStatus']
    
    if status != 'verified':
        while  status != 'verified':
    
            requests.post(url, headers=headers, json=a)
            
            print("Non verificato")
            time.sleep(10)
    else:
        urlOts = response.json()['file']
        download_ots.download(urlOts, otsFilename)
        print("Verified")
        delete_tmp_file.delete()
        print("All file deleted")
