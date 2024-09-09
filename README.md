# Interactive-Server-Client-application
This is an application with 1 server and 1 client, which can be used to send text documents and images.


Client code explained briefly
1. Connects to the server, requests a specific image for the serve.
2. It asks the client wether he wants a text document or image from the server.
3. It receives all the data from the server.
4. The received image will be in the client folder


Server code explained briefly
1. Creates a socket with a given IP and Port number and binds them.
2. If the client requests for file all the data is sent at once.
3. It receives the name of the file to be transfered from the server folder(i.e client requesting
for a specific file)
4. os package is used to check the availability of the requested image or text.

![image](https://user-images.githubusercontent.com/89318783/215668287-fafea6a2-6e8b-4bb7-90dd-0d89942d97ca.png)
