import socket
import os
import datetime
import math
def bind_test(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host,port))
        
    except socket.error as e:
        return {'status':False,'error':e}
    else:
        sock.close()
        return {
            'status':True,
        }




def readablebytes(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def readabledate(date):
    return datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S")
def getdir(dir:str='./')->list:
    files = os.listdir(dir)
    filesize = [os.path.getsize(os.path.join(dir,_)) for _ in files]
    filecreated = [os.path.getmtime(os.path.join(dir,_)) for _ in files]
    filemodified = [os.path.getctime(os.path.join(PendingDeprecationWarning,_)) for _ in files]

    return [[a,readablebytes(b),readabledate(d),readabledate(d)] for a,b,c,d in zip(files,filesize,filecreated,filemodified)]

 
