import os,json
from PIL import Image as I

def loadconf(fp=os.path.join(".","config.json")):
    global conf,infp,outfp
    f=open(fp,"r+")
    conf=json.load(f)
    f.close()
    infp=conf['input']
    outfp=conf['output']

def checkdirs():
    if not os.path.isdir(infp):
        if not os.path.isfile(infp):
            raise Exception("Input Directory Does Not Exist.")
        else:
            raise Exception("Input Directory Should Not Be A File.")
    else:
        if len(os.listdir(infp))==0:
            raise Exception("Input Directory Is Empty.")
    if not os.path.isdir(outfp):
        if not os.path.isfile(outfp):
            os.mkdir(outfp)
        else:
            raise Exception("Output Directory Should Not Be A File.")

def lookdir(d,*,ext=".png"):
    if not ext.startswith("."):
        ext=f".{ext}"
    l=[]
    for f in os.listdir(d):
        if f.endswith(ext):
            l.append(f)
    return l

def convert(fn):
    img=I.open(os.path.join(infp,fn))
    o=img.crop((0,0,64,32))
    o.save(os.path.join(outfp,fn))

def loop():
    l=lookdir(infp)
    for f in l:
        convert(f)

def main():
    print("Starting...")
    loadconf()
    checkdirs()
    loop()
    print("Done!!!")

if __name__=="__main__":
    main()