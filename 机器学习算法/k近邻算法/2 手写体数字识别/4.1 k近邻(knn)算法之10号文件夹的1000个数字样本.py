#k近邻(knn)算法之10号文件夹的1000个数字样本.py
#-*-coding:utf-8-*-
import numpy as np
import operator
import os  # 获取文件夹所有文件
# 从列方向扩张  tile(字典,(列数,1))
# 从行方向扩张  tile(字典,(行数,0))
def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0]  #  扩展行数，测试集行数与训练集行数一样
    # print(traindatasize)
    dif = np.tile(testdata, (traindatasize, 1)) - traindata# why 行数一致，是否确保所有训练集都与测试集计算
    # print(len(dif))
    sqdif = dif**2 #  差值平方
    sumsqdif = sqdif.sum(axis=1) #  平方求和，求出距离的平方
    distance = sumsqdif**0.5 #  开方，求出距离
    sortdistance = distance.argsort() # 距离升序
    sortdistance
    # print(len(sortdistance))
    # print(sortdistance)
    count = {}
    for i in range(0,k):
        # print(sortdistance[i])
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote,0) + 1  #  类别次数+1
    sortcount = sorted(count.items(),key=operator.itemgetter(1),reverse=True) # reverse降序,不懂
    return sortcount[0][0]  # 返回分类结果


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
    trainfile = os.listdir("train_digital_txt/10/") # 获取手写体图片名
    num = len(trainfile)
    # 长度784列，每一行存储一个文件
    # 以一个数组存储所有训练数据，行：文件总数，列：784
    trainarr = np.zeros((num ,784))
    print("所有txt文本数量:",num) #  num：所有txt文本数量
    print("相对路径：train_digital_pictures/10/") # 转换数据目录
    for i in range(0,num):
        thisfname = trainfile[i]
        thislabel = seplabel(thisfname)
        labels.append(thislabel)  # 记录txt文本对应的数字编号
        trainarr[i,:] = datatoarray("train_digital_txt/10/%s"  %(thisfname))# 加载txt文本数据    
    num = 0
    for arrs in trainarr: # 统计有用数据数量 
        for arr in arrs:
            if arr == 1:
                num += 1
                break
    print("统计有用数据数量 :",num)
    return trainarr, labels

# 用测试数据调用knn算法取测试，看是否能够准确识别
def testdata():
    trainarr, labels = traindata()
    for k in range(0,10):  # 遍历所有文夹
        print("相对路径：test_digital_txt/%s/" %(k)) # 转换数据目录
        testlist = os.listdir("test_digital_txt/%s/" %(k)) # 获取手写体图片名
     
        num = len(testlist)
        for i in range(0,num):
            thisfname = testlist[i]
            testarr = datatoarray("test_digital_txt/%s/%s"  %(k,thisfname))
            rknn = knn(21,testarr,trainarr,labels)
            print("%s样本预测结果：" %thisfname,rknn)
    
# 进行试验
testdata()
