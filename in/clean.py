import os,shutil

def lookdir(d=".",*,ext=".png"):
    if not ext.startswith("."):
        ext=f".{ext}"
    if not os.path.isdir(d):
        if not os.path.isfile(d):
            os.mkdir(d)
        return False
    l=[]
    for f in os.listdir(d):
        if f.endswith(ext):
            l.append(os.path.join(d,f))
    return l

def main():
    l=lookdir()
    for i in l:
        os.remove(i)
    try:
        shutil.rmtree(os.path.join("..","out"))
    except FileNotFoundError:
        pass

if __name__=="__main__":
    main()