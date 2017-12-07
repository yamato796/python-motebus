import socket
import sys,time
import threading, time
import json
ret=[]
my_threads=[]
cnt=0
    
def python_rpc(function,method,param,channel_ID,Prio,Sec):
    print '[INFO] Thread'+function+' '+str(channel_ID)+' start',time.strftime('%H:%M:%S')
    HOST = '127.0.0.1'
    PORT = 6060
    packet = json.dumps({"jsonrpc":"2.0","method":"XRPC.SendCall","params":[function,{"method":method,"params":param},Prio,Sec],"id":channel_ID},separators=(',', ':'),sort_keys=True)
    packet = packet+chr(10)
    global ret
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.sendall(packet)
    data = s.recv(1024)
    ret.insert(channel_ID -1,[data,function,channel_ID])

    time.sleep(5)
    s.close()
    flag = 0
    print '[INFO] Thread'+str(channel_ID)+' end',time.strftime('%H:%M:%S')

def send(func,method,param,prio,sec):
    global cnt
    global my_threads
    cnt=cnt+1
    thread1 = threading.Thread(target = python_rpc ,args=(func,method,param,cnt,prio,sec))
    my_threads.append(thread1)
    thread1.start()

def response():
    i =0
    for t in my_threads:
    	if t.isAlive():
    		i=i+1
    if i == len(my_threads):
    	return -1
    return ret

