import threading,time
import Motebus as motebus_rpc

foo = {"A":"12","B":"25"}


motebus_rpc.send("mote@127.0.0.1","add",[foo],10,8,15)
time.sleep(5)
print(motebus_rpc.response())
