import shutil
import os 


destination = './ots/'

def move_ots(ots):
    
    try:
        
        shutil.move(ots, destination)
        print("Trasferimento avvenuto")
    except:
    
        print("Trasferimento fallito")
