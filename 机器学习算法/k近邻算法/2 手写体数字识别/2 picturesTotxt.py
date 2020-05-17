# 训练集合和试集图片处理
# 先将所有图片转为固定狂傲，比如：28*28，然后转为文本
from PIL import Image
import os
def pictureTotxt(data_name): #  data_name:数据类型名称
    for i in range(0,10):  # 遍历所有文件夹
        print("%s_digital_pictures/%s/" %(data_name,i)) # 转换数据目录
        lists = os.listdir("%s_digital_pictures/%s/" %(data_name,i)) # 获取手写体图片名
        for list in lists: # 遍历所有图片
            # 打开手写体图片
            im = Image.open("%s_digital_pictures/%s/%s" % (data_name,i,list))
            # 打开txt文本
            fh = open("%s_digital_txt/%s/%s.txt" % (data_name,i,list.split(".")[0]),"a")
            width = im.size[0]  # 图片宽
            height = im.size[1]  #图片高
            for k in range(0,width):  #  存入txt文本
                for j in range(0,height):
                    cl = im.getpixel((k,j))  # bmp图片的像素只有一个数
                    if(cl == 0):  # 0：黑色
                        # 黑色为0
                        fh.write("0")
                    else:
                        # 白色为1
                        fh.write("1")
                fh.write("\n")        
            fh.close()
pictureTotxt("train")
pictureTotxt("test")
