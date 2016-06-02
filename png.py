from PIL import Image
import os

hou_img_src = ""
qian_img_src = ""
root=""
qian_W_num = 0
qian_H_num = 0

def getAllPhtots():
    global root, hou_img_src, qian_img_src
    root = os.getcwd() + "/"
    hou_img_src = root + 'hou.jpg'
    qian_img_src = root + 'qian.jpg'

def createNewImg():
    global hou_img_src, qian_img_src, qian_W_num, qian_H_num
    hou_img = Image.open(hou_img_src)
    qian_img = Image.open(qian_img_src)
    qian_W_num, qian_H_num = qian_img.size
    out_img = Image.new("RGBA",(qian_W_num, qian_H_num))
    for i in range(0, qian_W_num):
        for j in range(0, qian_H_num):
            avg1 = sum(qian_img.getpixel((i, j)))/3
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