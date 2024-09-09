import socket,os
from PIL import Image
PORT = 1234
IP = '127.0.0.2'
BSize=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))
s.listen(1)
print('Server has started. Waiting for connections....')
while True:
    conn, addr = s.accept()
    if conn:
        print(f'Connecting to {addr}...')
        k,_=conn.recvfrom(BSize)
        if k.decode('utf-8') == '2':
            image_name,_ = conn.recvfrom(BSize)
            name = str(image_name.decode('utf-8')[0:])
            path_of = "ServerFolder/" + name
            if os.path.isfile(path_of) == False:
                print("file not found\n")
            else:
                with open(f'ServerFolder/{name}', 'rb') as f:
                    conn.sendall(f.read())
                    f.close()
                    break
        if k.decode('utf-8')=='1':
            text_file_name,_=conn.recvfrom(BSize)
            name= str(text_file_name.decode('utf-8')[0:])
            path_of = "ServerFolder/" + name
            if os.path.isfile(path_of) == False:
                print("file not found\n")
            else:
                with open(f'ServerFolder/{name}', 'rb') as f:
                    conn.sendall(f.read())
                    f.close()
                    break
    print('TASK HAS FINISHED SUCCESSFULLY')
