
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import datetime
import threading
import time
from socket import *


def recvData(connectionSocket, clientAddr, streamServer):
    streamServer.open();
    while(True):
        serverNumberByteArray = connectionSocket.recv(4);
        serverNumber = int.from_bytes(serverNumberByteArray,byteorder = "little", signed = True);
        packetQuantityByteArray = connectionSocket.recv(4);
        packetQuantity = int.from_bytes(packetQuantityByteArray, byteorder = 'little', signed = True);
        x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f');
        y = packetQuantity;
        streamServer.write(dict(x=x, y=y));


def StartNetwork(bindingSocket, streamServerArray):
    count = 0;
    while(True):
        print("waitingAccept");
        connectionSocket, clientAddr = serverSock.accept();
        print("waitingAccept");
        threading.Thread(target = recvData, args=(connectionSocket,clientAddr,streamServerArray[count])).start();
        count+=1;

stream_ids = tls.get_credentials_file()['stream_ids'] // plotly 로부터 받은 토큰
print(stream_ids);

username = 'kaiose' // 입력
api_key = "1234567"; // 입력

py.sign_in(username, api_key);



size = len(stream_ids);

colorArray = ['red','blue','green']
streamArray = [];
traceArray = [];

streamingServerArray = [];
for i in range(0,size):
    streamArray.append(go.Stream(token = stream_ids[i], maxpoints = 80));
    traceArray.append(go.Scatter(go.Scatter(x=[],y=[], mode ='lines+markers', stream= streamArray[i], marker = { 'color' : colorArray[i%3]}, name = 'Server'+str(i) )));
    streamingServerArray.append(py.Stream(stream_ids[i]));

data = go.Data(traceArray);

layout = go.Layout(title='Traffic Level');

fig = go.Figure(data=data, layout= layout);

py.plot(fig,filename='Traffice Streaming');

serverSock = socket(AF_INET, SOCK_STREAM);
serverSock.bind(('',8000));
serverSock.listen(5);

StartNetwork(serverSock,streamingServerArray);




#for token in streamingServerArray:
#    token.close();
 
#stream_1 = go.Stream(
#    token = stream_id[0],
#    maxpoints = 80);
#stream_2 = go.Stream(
#    token = stream_ids[1],
#    maxpoints = 80);

#trace1 = go.Scatter(x=[],y=[], mode ='lines+markers', stream= stream_1, marker = { 'color' : 'red'}, name = 'Server1');
#trace2 = go.Scatter(x=[],y=[], mode ='lines+markers', stream= stream_2, marker = { 'color' : 'blue'}, name = 'Server2');

#data = go.Data([trace1, trace2]);

#layout = go.Layout(title='Traffic Level');

#fig = go.Figure(data=data, layout= layout);

#py.plot(fig,filename='Traffice Streaming');

#s = py.Stream(stream_ids[0])
#s2 = py.Stream(stream_ids[1])
#s.open();
#s2.open();
#i = 0;
#k = 5;
#p = 1;
#q = 4;
#time.sleep(5)
#while(True):
    
#    serverNumberByteArray = sock.recv(4);
#    serverNumber = int.from_bytes(serverNumberByteArray,byteorder="little",signed = True);
#    packetQuantityByteArray = sock.recv(4);
#    packetQuantity = int.from_bytes(packetQuantityByteArray, byteorder="little",signed = True);
#    serverNumberByteArray2 = sock2.recv(4);
#    serverNumber2 = int.from_bytes(serverNumberByteArray2,byteorder="little",signed = True);
#    packetQuantityByteArray2 = sock2.recv(4);
#    packetQuantity2 = int.from_bytes(packetQuantityByteArray2, byteorder="little",signed = True);



#    print("serverNumber : " + str(serverNumber) + " packetQuantity : " + str(packetQuantity));
#    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f');
#    y = packetQuantity;
#    #y = (np.cos(k*i/50)*np.cos(i/50)+np.random.randn(1))[0]
#    y2 = packetQuantity2;
#    #y2 = (np.cos(p*q/50)*np.cos(p/50)+np.random.randn(1))[0]
    
#    s.write(dict(x=x,y=y));
#    s2.write(dict(x=x,y=y2));
#    time.sleep(1)

#s.close();
#s2.close();
