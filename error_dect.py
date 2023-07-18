import paramiko
from telegram import *
import time
import logging


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
        error_msg = ''
    else: 
        error_msg = 'There is an error'
    if output == '':
        out_message = 'There is no output'
    else: 
        out_message = 'output detected'
        

logging.basicConfig(filename="logging_info.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.INFO) 


total_time = 0

while(total_time <= 10):
    total_time += 1
    if out_message == "output detected":
        telebot('',out_message)
        logging.info('output detected')
    else:
        telebot(error_msg, out_message)
        logging.info('There was no output detected, an error was also detected')
    time.sleep(60)

# ssh kuka@172.27.5.126