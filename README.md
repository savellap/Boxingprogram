# Communication Contract
Requesting data through the microservice
----------------------------------------------------
socket.send_string()
This is how to request data from the microservice by sending a string
After the data has been dispatched, the microservice will send a response

How data is received through the microservice
----------------------------------------------------
message_received = socket.recv_string()
This command above demonstrates how to receive data thorugh the microservice.


![image](https://user-images.githubusercontent.com/102436128/218686921-80abe957-111f-4610-88db-6560e88752d2.png)
