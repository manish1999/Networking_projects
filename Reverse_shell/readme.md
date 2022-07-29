Reverse shell is a networking tool which is used to connect two or more host computers in which one acts as a server and other acts as a client to perform CLI(Command Line Interface) operations.
 Here in the project, I'm developing a single client reverse shell program through socket programming using python. 
The basic idea behind the project concept is that when the client side code is executed on the client’s machine, a connection is established between the server and client using the socket declared in the code. Given that the server is listening on that particular port mentioned prior to the client side code execution. 
Once the connection is established, the server will be able to execute the CLI commands remotely.
 Example:- bash(linux),powershell(windows). 
After the execution is completed, the connection is terminated and the reserved port is released. 

//To run the program in terminal
client side
-- python client.py
server side
--python server.py


///change port number accordingly.


//@Manish Dhal Samanta//
Instagram: m07xh
Github: https://github.com/manish1999/
Linkedin: https://www.linkedin.com/in/manish-dhal-samanta-13872b63/