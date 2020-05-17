import os
import numpy as np
import operator
# 加载txt文本数据
def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0,28):
        thisline = fh.readline()
        for j in range(0,28):
            arr.append(int(thisline[j]))
    fh.close()
    return arr
# 建立取文件名前缀函数
def seplabel(fname):
    filestr = fname.split(".")[0]
    label = int(filestr.split("_")[0])
    return label
# 建立训练数据
def traindata():
    labels = []
    num = 0
    for j in range(0,10):  # 遍历所有图片文件
        trainfile = os.listdir("train_digital_txt/%s/" %(j)) # 获取手写体图片名
        num = len(trainfile) + num
    # 长度784列，每一行存储一个文件
    # 以一个数组存储所有训练数据，行：文件总数，列：784
    trainarr = np.zeros((num,784))
    print(num) #  num：所有txt文本数量
    for k in range(9,10):  # 遍历所有文件夹
        print("train_digital_pictures/%s/" %(k)) # 转换数据目录
        trainfile = os.listdir("train_digital_txt/%s/" %(k)) # 获取手写体图片名    
        num = len(trainfile)
        for i in range(0,num):
            thisfname = trainfile[i]
            thislabel = seplabel(thisfname)
            labels.append(thislabel)  # 记录txt文本对应的数字编号
            trainarr[i,:] = datatoarray("train_digital_txt/%s/%s"  %(k,thisfname))# 加载txt文本数据
    print(len(labels))
    num = 0
    for arrs in trainarr: # 统计有用数据数量 
        for arr in arrs:
            if arr == 1:
                num += 1
                break
    print(num)
    return trainarr, labels
# 进行训练
trainarr, labels = traindata()

