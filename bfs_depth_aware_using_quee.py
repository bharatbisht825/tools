import os
from collections import deque

def bfsWalk():
    currentDepth=0
    q=deque([0,"/home/bharat.singh@SUHORA.LOCAL/Documents/Sunshine_Demo"]) 
    # to make it depth aware
    directoryDict={}
    while(len(q)>0):
        dir=q.popleft()
        if(type(dir)==int):
            currentDepth=dir
            continue
        dirSet=set()
        dirList=[]
        for e in os.scandir(dir):
            if e.is_dir():
                dirSet.add(e.name)
                dirList.append(e.path)
        directoryDict[dir]=[dirSet,currentDepth]
        q.append(currentDepth+1)
        q.extend(dirList)
    for key,value in directoryDict.items():
        print(key,value)
bfsWalk()
