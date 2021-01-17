from PIL import Image as I

def main():
    img=I.open("in.png")
    o=img.crop((0,0,64,32))
    o.save("out.png")

def init():
    print("Starting...")
    main()
    print("Done!!!")

if __name__=="__main__":
    init()