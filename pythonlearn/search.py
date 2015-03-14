import os

def search(word,curdir):

    files=[x for x in os.listdir(curdir) if os.path.isfile(x)]
    dirs=[x for x in os.listdir(curdir) if os.path.isdir(x)]

    for filename in files:
        if word in filename:
            print os.path.join(curdir,filename)
    #print dirs
    for dirname in dirs:
        search(word,os.path.join(curdir,dirname))


search('e',os.path.curdir)
