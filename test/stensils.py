from PIL import Image
ima = Image.open("/Users/glebsvarcer/Desktop/my-stupid-little-programs/test/Schematic-illustration-of-the-principles-of-AFM-The-scanner-is-composed-of-three-piezo.png")
im = ima.load()
bwh = Image.new(mode="RGB",size=ima.size)
bw = bwh.load()
for x in range(ima.size[0]):
    for y in range(ima.size[1]):
        s = sum(im[x,y])//3#%128*255
        bw[x,y] = (s,s,s)

bwh.show()