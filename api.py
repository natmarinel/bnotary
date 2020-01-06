import requests

#alla funzione viene passata variabile event.src_path di check_new_file.py 
def api_bnotary(file):
    apikey= '3791c1164af2f63e72ea87bf01c7059f9b7b43a4ad53f0c3e80c0ebd7f531c28'
    url = 'https://notaryb-api.bcademy.it/api/v1/upload/file'
    payload = {'hash': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'hashType': 'SHA-256'}
    files = {'file': (file , open(file, 'r'), )}
    print(files)
    #chiamata di tipo post a api bnotary
    response = requests.post(url,verify=False, headers={'apiKey':apikey, 'Content-Type': 'application/x-www-form-urlencoded'},data=files )

    print(response.status_code)
    #ritorna come risposta un json
    #print(response.json())
    #print(requests.post(url).json())
