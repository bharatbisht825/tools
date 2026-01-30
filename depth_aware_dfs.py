
def dfsWalk(dir,curDepth,maxDepth):
    dirList=[]
    for e in os.scandir(dir):
        if e.is_dir():
            dirList.append(e.path)
    if(len(dirList)==0 or curDepth==maxDepth):
        return
    for dir in dirList:
        dfsWalk(dir,curDepth+1,maxDepth)
        if(curDepth==maxDepth-1):
            print(dir)
dfsWalk("/home/bharat.singh@SUHORA.LOCAL/Documents/Sunshine_Demo/ICEYE_Processed",0,2)
