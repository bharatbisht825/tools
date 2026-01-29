import os
from collections import deque

def bfsWalk():
    q=deque(["/home/bharat.singh@SUHORA.LOCAL/Documents/Sunshine_Demo"]) 
    # to make it depth aware
    baseDepth=len("/home/bharat.singh@SUHORA.LOCAL/Documents/Sunshine_Demo".split("/"))
    directoryDict={}
    while(len(q)>0):
        dir=q.popleft()
        depth=(len(dir.split("/"))-baseDepth)
        dirSet=set()
        dirList=[]
        for e in os.scandir(dir):
            if e.is_dir():
                dirSet.add(e.name)
                dirList.append(e.path)
        directoryDict[dir]=[dirSet,depth]
        q.extend(dirList)
    for key,value in directoryDict.items():
        print(key,value)
bfsWalk()
