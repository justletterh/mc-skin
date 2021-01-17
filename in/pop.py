import random,os

def gen_name(n,*,ext=".png"):
    if type(n)==float:
        n=int(round(n,0))
    l=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    o=""
    for i in range(n):
        o+=random.choice(l)
    o+=ext
    return o

def gen_names(n,nn=None):
    if nn is None:
        nn=n
    o=[]
    for i in range(n):
        o.append(gen_name(nn))
    return o

def main():
    res=gen_names(100,30)
    for i in res:
        os.system(f"curl https://raw.githubusercontent.com/justletterh/mc-skin/main/in.png -so {os.path.join('.',i)}")


if __name__=="__main__":
    main()