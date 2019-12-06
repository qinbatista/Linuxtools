    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
from socket import socket, AF_INET, SOCK_STREAM
import os
import hashlib
from os.path import join, getsize
class SyncServer:
    def startServer(self,port):
        tcpSerSock=socket(AF_INET,SOCK_STREAM)
        tcpSerSock.bind(("",port))
        tcpSerSock.listen(5)
        while True:
            try:
                self.tcpCliSock,self.addr =tcpSerSock.accept()
                print("[Server Msg]"+self.addr[0]+" Connecting" )
                self.ReciveFiles()
            except:
                pass
            finally:
                self.tcpCliSock.close()
        tcpSerSock.close()
    def getBigFileMD5(self,filepath):
        if os.path.isfile(filepath):
            md5obj = hashlib.md5()
            maxbuf = 8192
            f = open(filepath,'rb')
            while True:
                buf = f.read(maxbuf)
                if not buf:
                    break
                md5obj.update(buf)
            f.close()
            hash = md5obj.hexdigest()
            return str(hash).upper()
    def AnalysisHeader(self):
        #获取文件名
        filename_len = self.tcpCliSock.recv(2).decode("utf8")
        filename = self.tcpCliSock.recv(int(filename_len)).decode("utf8")
        filename=filename.replace("π","")
        #获取md5
        md5Length = self.tcpCliSock.recv(2)
        md5Length = int(md5Length.decode()) #python3
        md5Name = self.tcpCliSock.recv(md5Length).decode("utf8")
        #获取文件大小
        fileszie_len = self.tcpCliSock.recv(1)
        fileszie_len = int(fileszie_len.decode()) #python3
        filesize = self.tcpCliSock.recv(fileszie_len).decode("utf8")
        self.tcpCliSock.send(("HEADER").encode())
        return filename,md5Name,filesize
    def ReciveFiles(self):
        filename,md5Name,filesize = self.AnalysisHeader()
        strfilesize = int(filesize)
        total = 0
        with open(filename, 'wb') as f:
            while strfilesize!=0:
                buf = self.tcpCliSock.recv(1024)
                total = total+1024
                f.write(buf)
                if strfilesize>1024:
                    strfilesize = strfilesize-1024
                else:
                    strfilesize=0
                print("[Server msg] recived "+str(total)+" bit, remaining"+str(strfilesize))
        if self.getBigFileMD5(filename) == md5Name and getsize(filename) ==int(filesize):
            self.tcpCliSock.send(("DONE").encode())
            print("[Server Msg]"+self.addr[0]+" Sent successed: "+filename+" MD5(Local):"+self.getBigFileMD5(filename)+" FileSize(Local):"+str(getsize(filename)))
            print("[Server Msg]"+self.addr[0]+" Sent successed: "+filename+" MD5(Remote):"+md5Name+" FileSize(Remote):"+filesize)
        else:
            self.tcpCliSock.send(("Failed").encode())
            print("[Server Msg]"+self.addr[0]+" Sent Failed: "+filename+" MD5(Local):"+self.getBigFileMD5(filename)+" FileSize(Local):"+str(getsize(filename)))
            print("[Server Msg]"+self.addr[0]+" Sent Failed: "+filename+" MD5(Remote):"+md5Name+" FileSize(Remote):"+filesize)

if __name__ == '__main__':
    print("[Server msg] Start...")
    s = SyncServer()
    s.startServer(1234)
    print("[Server msg] End...")