#script to upload file through bnotary api
#use request to upload file 
#pass to the request  file's hash, hash type and filename
import requests
import json
import hashlib
import verify_file

def call_api(file):
    
    print("Inizio chiamata api bnotary\n")
    
    url = 'https://notaryb-api.bcademy.it/api/v1/upload/file'
    apiKey = '3581ca332d59abbbb665c6ec993642ab8c576b06e95e7a916e06edd6fd9b49ba'
    headers = {'apiKey' : apiKey, 'Content-Type' : 'application/x-www-form-urlencoded'}
    file = file.replace('./file_to_be_notarized/','')
    hashFile = file.encode('utf-8')
    hashFile = hashlib.sha256(hashFile).hexdigest()
    print(hashFile)
    hash = {'hash': hashFile, 'hashType' : 'SHA-256', 'filename': file }
    #file = {'key':'file', 'type':'file', 'src': file}
    #file = {file : (file , open(file,'rb'), 'application/x-www-form-urlencoded', {'originalname': file})} 
    print(type(file))
    print("File passato a request\n",file)
    response = requests.post(url, headers=headers, data=hash)
    
    print("Url della richiesta",response.request.url)
    print("Header della richiesta:\n", response.request.headers)
    print("Body della richiesta: \n",response.request.body)
    print("Status code risposta:\n",response.status_code)
    print("Response header:\n", response.headers)
    print("Response Body:\n" ,response)
    print("Json risposta\n", response.json())

    timestamp = response.json()['timestamp']
    ots = response.json()['otsFilename']
    Hash = response.json()['hash']
    print("Timestamp:\n",timestamp)
    print(type(timestamp))
    print("File Ots:\n",ots)
    print(type(ots))
    print("Hash file:\n", Hash)
    print(type(Hash))
    print("Inizio chiamata a verify\n")
    #call to verify_file.py
    verify_file.verify(Hash, ots, timestamp)
    



#try:
        #open('./ots/'+ots, 'wb').write(response.content)
        #print("OK file saved\n")
        #print("Inizio chiamata a verify\n")
        #verify_file.verify(hash, ots, timestamp)
    #except Exception as e:
       
        #print("No file saved")
        #print(e)
