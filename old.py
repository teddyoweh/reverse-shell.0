class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
       
 
    

        self.threadpool = QThreadPool()

        landing = QHBoxLayout()
        serverhostlabel = QLabel()
        serverhostlabel.setText("Server Host:")
        landing.addWidget(serverhostlabel)
        serverhostlabel.setFixedWidth(100)

        self.serverhost = QLineEdit()
        self.serverhost.setText("localhost")
        self.serverhost.setFixedWidth(200)
        landing.addWidget(self.serverhost)

        serverportlabel = QLabel()
        serverportlabel.setText("Server Port:")
        serverportlabel.setFixedWidth(100)
        landing.addWidget(serverportlabel)

        self.serverport = QLineEdit()
        self.serverport.setFixedWidth(200)
        landing.addWidget(self.serverport)
  
        

        self.connectbutton = QPushButton("Connect")
        self.connectbutton.setFixedWidth(100)
        self.connectbutton.clicked.connect(self.connecttoserver)
        landing.addWidget(self.connectbutton)
        landing.addStretch()
        container = QWidget()
        self.appframe = QWidget()
        self.appvbox = QVBoxLayout()

        apptitlelabel = QLabel()
        apptitlelabel.setText("My App")
        apptitlelabel.setFixedWidth(100)
        self.appvbox.addWidget(apptitlelabel)
        self.appframe.setLayout(self.appvbox)


        container.setLayout(landing)
    

        self.setCentralWidget(container)
        self.showMaximized()
    def connecttoserver(self):
        try:
            host, port =self.serverhost.text(), int(self.serverport.text())
            if(len(host)<3):
                lg = QMessageBox(self)
                dlg.setWindowTitle("IP Address Error")
                dlg.setText(f'Invalid IP address Format')
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()

        except ValueError as e:
            print("Invalid port number")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Value Error")
            dlg.setText(f'{e}')
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
        else:
            bndtst = bind_test(host,port)
            if(bndtst['status']==False):

                self.errormsgbox = QMessageBox()
                self.errormsgbox.setWindowTitle("Connection Error")
                self.errormsgbox.setText(f"{bndtst['error']}")
                self.errormsgbox.setIcon(QMessageBox.Icon.Warning)
                self.errormsgbox.exec()
            
            else:
                if port not in range(0,65535):
                    self.errormsgbox = QMessageBox()
                    self.errormsgbox.setWindowTitle("Port Error")
                    self.errormsgbox.setText(f"Overflow Error: port must be 0-65535.")
                    self.errormsgbox.setIcon(QMessageBox.Icon.Warning)
                    self.errormsgbox.exec()
                else:

                    self.host,self.port = host,port
                    #self.threadpool.start(ServerCLI(self,host,port))
                    serverthread = threading.Thread(target=Server, args=(self,host,port))
                    startedthread = threading.Thread(target=self.start_server)
                    serverthread.start()
                    startedthread.start()
                    serverthread.join()
                    startedthread.join()
         



    def start_server(self):
        print('lol')
        self.connectbutton.setText('Listening')
        self.connectbutton.setEnabled(False)

      
        