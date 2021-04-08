import paramiko

hostname = '192.168.0.202'
username = "root"
password = "zhongxin@201!god"
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password, compress=True, allow_agent=False, look_for_keys=False)
sftp_client = client.open_sftp()
remote_file = sftp_client.open("/data/logs/pigx-upms-biz.log")

try:
    for line in remote_file:
        print(line)
finally:
    remote_file.close()
