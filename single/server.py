import socket
import sys




class Server(object):
    def __init__(self,ui,host,port):
        self.ui_sys = ui
        self.host = host
        self.port = port
        self.socket_create()
        self.socket_bind()
        self.socket_accept()
    def socket_create(self):
        try:
            
            self.s = socket.socket()
        except socket.error as msg:
            print("Socket creation error: " + str(msg))
    def socket_bind(self):
        print("Binding socket to port: " + str(self.port))
        self.s.bind((self.host, self.port))
        self.s.listen(5)
    def socket_accept(self):
        self.conn, self.address = self.s.accept()
        print("Connection has been established | " + "IP " + self.address[0] + " | Port " + str(self.address[1]))
        #self.send_commands(self.conn)
        #self.conn.close()
    def send_commands(self,cmd):

   
        if self.cmd == 'quit':
            self.conn.close()
            self.s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            self.conn.send(str.encode(cmd))
            client_response = str(self.conn.recv(1024), "utf-8")
            print(client_response, end="")
            return client_response

      

        
    
