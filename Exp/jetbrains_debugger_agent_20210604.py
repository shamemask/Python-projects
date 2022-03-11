import paramiko


server_auth = {
    'hostname': '10.100.24.28',
    'username': 'eapteka\d.artamonov2',
    'password': 'Df4kq-poECW1'
}

with paramiko.SSHClient() as ssh:
    ssh.connect(**server_auth)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    stdin, stdout, stderr = ssh.exec_command('psexec -d -c \\* -u eapteka\d.artamonov2  -p Df4kq-poECW1 -h C:\Users\dartamonov\Documents\Git\Python\Python\junior\subjects.txt')

    print(stdout.read().decode())  # читать нужно, пока открыт ssh
