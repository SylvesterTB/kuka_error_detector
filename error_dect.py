import paramiko

hostname = '172.27.5.126'
port = 22

username = 'kuka'
password = 'kuka'

cmd = 'update-agent'

with paramiko.SSHClient() as client:

    client.load_system_host_keys()
    client.connect(hostname, port, username, password)

    (stdin, stdout, stderr) = client.exec_command(cmd)

    output = stdout.read()
    print("output:"+str(output, 'utf8'))

    error = stderr.read()
    print("error:"+str(error, 'utf8'))

    if error == '':
        print('no error')
    else: 
        print('There is an error, send message vie telegram')
    if output == '':
        print('There is no output')
    else: 
        print('output detected')


# ssh kuka@172.27.5.126