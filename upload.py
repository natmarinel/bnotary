import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/nat/Scrivania/Bcademy/AWS/giulio_webdev.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
transport = paramiko.Transport(("34.244.128.153"))



# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname="34.244.128.153", username="ubuntu", pkey=key)
    print("Connessione avvenuta")
    client.put('index.php', '/var/www/bitagora_files')
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('index.php', '/var/www/bitagora_files/index.php')

    # close the client connection once the job is done
    client.close()

except Exception as e:
    print (e)