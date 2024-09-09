import socket
from PIL import Image
IP = '127.0.0.2'
PORT = 1234
BSize=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print("Connecting to the server...\n")
k=int(input("1.Text file\n2. Image\n >>"))
s.sendto(str(k).encode(),(IP,PORT))
if k == 2:
        image_name=input('which image do you want from the server(with the extension):')
        receiving_name = input('what do you want to name the new image(with extension):')
        s.sendto(image_name.encode(),(IP,PORT))
        with open(f'ClientFolder/{receiving_name}', 'wb') as f:
                print('New file has been created to save the image received')
                data = s.recv(100000)
                f.write(data)
                print("DATA HAS RECEIVED") 
                f.close()
        # with open(f'ClientFolder/{received_name}', 'rb') as f:
        #         im = Image.open(f)
        #         im.show()

        print('IMAGE IS RECEIVED')
        s.close()
if k==1:
        text_file_name=input('which file do you want from the sever(with extension):')
        rec_text_file_name=input('what do you want to name the new image(with extension):')
        s.sendto(text_file_name.encode(),(IP,PORT))
        with open(f'ClientFolder/{receiving_name}', 'wb') as f:
                print('New file has been created to save the image received')
                data = s.recv(100000)
                f.write(data)
                print("DATA HAS RECEIVED") 
                f.close()

print('TASK HAS FINISHED SUCCESSFULLY')
