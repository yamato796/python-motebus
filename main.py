import threading,time
import Py_Motebus as motebus_rpc


#motebus_rpc.send("AIlab@127.0.0.1","time",["now is"],10,6)
#time.sleep(1)
#motebus_rpc.send("app1@127.0.0.1","hello",["test1","test2"],10,60)
#time.sleep(1)
#motebus_rpc.send("AIlab@127.0.0.1","hello",["test1","test2"],10,6)

#motebus_rpc.send("OpenCV@192.168.1.21","FaceDetection",['./mona.png'],10,6)
#motebus_rpc.send("OpenCV@192.168.1.21","GreyScale",['./mona.png'],10,6)
motebus_rpc.send("opencv@192.168.1.21","Resize",['./mona.png',100,100],10,6)
#print('poi poi poi poi')
#print('poi poi poi poi')

#time.sleep(75)
while(motebus_rpc.response()== -1):
	continue
print(motebus_rpc.response())
print('poi poi poi poi')
print('poi poi poi poi')
print('poi poi poi poi')
