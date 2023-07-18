import paramiko
from telegram_2 import *
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
        

logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

run_amt = input('how many times do you want the program to run?')
usr_time = input('how often do you want the prgram to run (in seconds)?')
run_amt = int(run_amt)
usr_time = int(usr_time)
total_time = 0

while(total_time <= run_amt-1):
    total_time += 1
    if out_message == "output detected":
        telebot('',out_message)
        logging.debug('output detected')
    else:
        telebot(error_msg, out_message)
        logging.debug('There was no output detected, an error was also detected')
    time.sleep(usr_time)

# ssh kuka@172.27.5.126