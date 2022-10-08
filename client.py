print('Starting....')

import lib
lib.log('*','LIB Initialized..')
lib.log('*','Initializing [Socket, Threading, Sys]...')
import socket
from threading import Thread
import sys
import os

#Example Token: ('2ade65e8b2860acdfa76ff7520c8aa785ddeb992', 'Omena0')

#sus

def hang():
    input('Press ENTER to close...')
    os._exit(0)
    sys.exit(0)

authip   = '192.168.0.104'
authport =  1234

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

lib.log('*','Connecting to AUTH-SERVER...')
try: s.connect((authip,authport))
except:
    lib.log('!','Failed to connect to AUTH-SERVER!')
    hang()

username = input('Username: ')
password = input('Password: ')

lib.log('*','Authenticating...')

s.send(f'? {username} {lib.hash(password)}'.encode())

answer = s.recv(32767).decode().replace('X ','')

if answer == 'Invalid_Password':
    lib.log('!','Invalid Password! (X Invalid_Password)')
    hang()
elif answer == 'No_User':
    lib.log('!','Invalid Username! (X No_User)')
    if input('Create user? (Y/N)').lower() == 'y':
        s = socket.socket()
        s.connect((authip,authport))
        s.send(f'+ {username} {password}'.encode())
        msg = s.recv(32767).decode()
        if msg == 'X User_Exists':
            lib.log('!','User already exists with same username!')
        elif msg == 'X User_Created':
            lib.log('!','User created! Logging in...')
            s = socket.socket()
            s.connect((authip,authport))
            s.send(f'? {username} {lib.hash(password)}'.encode())
            answer = s.recv(32767).decode().replace('X ','')
            token = answer
            print(token)
            lib.log('+',f'Logged in as {username}')


else:
    token = answer
    print(token)
    lib.log('+',f'Logged in as {username}')

s = socket.socket()

ip = input('IP: ')
port = input('PORT: ')

if ip == '': ip = '192.168.0.104'
if port == '': port = 5000

if ip == authip and port == authport:
    lib.log('!','IP and PORT cannot be the same as AUTH-ADDRESS.')
    hang()

def message_handler():
    while True:
        s.send((input()+'<TOKEN>'+token).encode())



s.connect((ip,int(port)))
s.send(('<TOKEN>'+token).encode())

a = Thread(target=message_handler)
a.daemon = True
a.start()

while True:
    msg = s.recv(2096).decode()
    msg = msg.split('<SEP>')
    lib.log(msg[0],msg[1])












