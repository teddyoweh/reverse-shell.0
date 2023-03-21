import sys
import socket
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from server import ServerCLI
from helpers import bind_test,getdir
from single.server import Server
import threading
import pandas as pd
import os
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
       
        self.container = QWidget()
     
        self.landing = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(FileSystemView(),"File System")
        self.tabs.addTab(self.tab2,"Terminal")
        self.tabs.addTab(self.tab3,"Screenshots")
        self.tabs.addTab(self.tab4,"Keylogger")
        self.tabs.addTab(self.tab1,"Networking")



        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        self.landing.addWidget(self.tabs)
        self.container.setLayout(self.landing)
    

        self.setCentralWidget(self.container)
        self.showMaximized()

     
class FileSystemView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.list = QTableView()
  

        self.layout.addWidget(QLabel("File System"))
        headerframe =   QWidget()
        headerlayout = QHBoxLayout()
        headerframe.setLayout(headerlayout)
        self.cwdinput = QLineEdit()

        self.cwdinput.setText(os.getcwd())
        refereshbtn=  QPushButton()
        refereshbtn.setText("Refresh")  
        refereshbtn.clicked.connect(self.refereshbtnaction)
        headerlayout.addWidget(self.cwdinput)
        headerlayout.addWidget( refereshbtn) 
        self.layout.addWidget(headerframe)
        header = self.list.horizontalHeader()
        self.list.setWordWrap(True)
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        #header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        #header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
   
        
        self.data =getdir(os.getcwd())
        data = pd.DataFrame(self.data,columns=['Names','File Size','Created at','Modified at'],index=[_ for _ in range(len(self.data))])
        self.model = FileSystemModel(data)
        self.list.setModel(self.model)

        self.layout.addWidget(self.list)
        self.setLayout(self.layout)
    def refereshbtnaction(self):
        try:
            self.data =getdir(dir=self.cwdinput.text())
            data = pd.DataFrame(self.data,columns=['Names','File Size','Created at','Modified at'],index=[_ for _ in range(len(self.data))])
            self.model = FileSystemModel(data)
            self.list.setModel(self.model)
        except FileNotFoundError as e:
            dlg = QMessageBox(self)
            dlg.setWindowTitle(" FileNotFoundError")
            dlg.setText(f'{e}')
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()


class FileSystemModel(QAbstractTableModel):

    def __init__(self, data):
        super(FileSystemModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

 

      
        
       
               

 



app = QApplication(sys.argv)

window = MainWindow()
 

 

window.show()

app.exec()