import os

subPath ="G:\\共享云端硬盘\\Media Center"

'''
for x in os.listdir(subPath):
    dirList = os.path.join(subPath,x)
    if os.path.isdir(dirList):
        if x == "movies":
            print(x)
'''       
def findSubs(xdir):
    for x in os.listdir(xdir):
        dirList = os.path.join(xdir,x)
        if os.path.isdir(dirList):
            if x == "Subs":
                for y in os.listdir(dirList):
                    files = os.path.join(dirList,y)
                    os.remove(files)
                print("ok " + dirList + " removed")
                os.rmdir(dirList)
            else:
                findSubs(dirList)

findSubs(subPath)

