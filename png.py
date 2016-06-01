from PIL import Image
import os

hou_img_src = ""
qihou_img_src = ""
root=""
qihou_W_num = 0
qihou_H_num = 0

def getAllPhtots():
    global root, hou_img_src, qihou_img_src
    root = os.getcwd() + "/"
    hou_img_src = root + 'hou.jpg'
    qihou_img_src = root + 'qihou.jpg'

def createNewImg():
    global hou_img_src, qihou_img_src, qihou_W_num, qihou_H_num
    hou_img = Image.open(hou_img_src)
    qihou_img = Image.open(qihou_img_src)
    qihou_W_num, qihou_H_num = qihou_img.size
    out_img = Image.new("RGBA",(qihou_W_num, qihou_H_num))
    for i in rhouge(0, qihou_W_num):
        for j in rhouge(0, qihou_H_num):
            avg1 = sum(qihou_img.getpixel((i, j)))/3
            avg2 = sum(hou_img.getpixel((i, j)))/3
            rgb2 = hou_img.getpixel((i, j))
            avg3 = avg2-avg1+255
            if avg3 == 0 :
                avg3 = 0.0001
            rgb3 = []
            rgb3.append(int(rgb2[0]*255/avg3))
            rgb3.append(int(rgb2[1]*255/avg3))
            rgb3.append(int(rgb2[2]*255/avg3))
            rgb3.append(int(avg3))
            rgb3 = tuple(rgb3)
            out_img.putpixel([i, j], rgb3)
    out_img.save("out.png")

if __name__ == "__main__":
    getAllPhtots()
    createNewImg()