import paramiko

HOST = "EC2_HOST"
USERNAME = "EC2_USERNAME"
KEY = "PRIVATE_KEY"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY
)

command = """
cd /home/ec2-user/project &&
git pull &&
pip3 install -r requirements.txt &&
python3 app.py
"""

stdin, stdout, stderr = client.exec_command(command)

print(stdout.read().decode())
print(stderr.read().decode())

client.close()

print("Deployment Completed")
