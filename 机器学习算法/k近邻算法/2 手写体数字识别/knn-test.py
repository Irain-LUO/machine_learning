def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0,28):
        thisline = fh.readline()
        for j in range(0,28):
            arr.append(int(thisline[j]))
    fh.close()
    return arr
def traindata_1000(): # 每个数字（0~9）前一百个txt文本存入同一个文件夹“10”
    import shutil
    import os
    for k in range(0,10): 
        docus = os.listdir("train_digital_txt/%s/" %(k)) # 获取txt
        for i in range(0,100):
            shutil.copyfile("train_digital_txt/%s/%s_%s.txt"  %(k,k,i),"train_digital_txt/10/%s_%s.txt"  %(k,i) )



def traindata_all(): # 每个数字（0~9）所有训练txt文本存入同一个文件夹“11”
    import shutil
    import os
    for k in range(0,10):
        docus = os.listdir("train_digital_txt/%s/" %(k)) # 获取txt
        for docus in docus:
             shutil.copyfile("train_digital_txt/%s/%s"  %(k,docus),"train_digital_txt/11/%s"  %(docus) )

def QR_Code(): # 二维码.jpg 转换成txt文本
    from PIL import Image
    fh = open("knn_test/二维码.txt","a")  # 打开txt文本
    im = Image.open("knn_test/二维码.jpg") # 打开二维码图片
    print("图片像素大小" , im.size)  # 打印图片像素大小
    width = im.size[0] 
    height = im.size[1]
    k = im.getpixel((1,9))  #  行：1，列：9的像素
    print("黑色",k)
    for i in range(0,width):  #  存入txt文件
        for j in range(0,height):
            cl = im.getpixel((i,j))# jpg图片返回list类型：三基色红绿蓝
            clall = cl[0] + cl[1] + cl[2] 
            if(clall == 0): # 三基色都为0，则黑色
                # 黑色为1
                fh.write("1")
            else:
                # 白色为0
                fh.write("0")
        fh.write("\n")
    fh.close

def calculate_txt_nums():  # 计算每个文件夹（0~9）的txt文本数量
    import os
    for i in range(0,10):
        nums = os.listdir("train_digital_txt/%s" %i)
        print("train_digital_txt/%s的txt数量:" %i,len(nums))

def accuracy_rating_classify():  # 获得6600训练集和2200测试集
    import shutil
    import os
    if not os.path.exists("test_digital_txt/testdata_0.25"):
        os.mkdir("test_digital_txt/testdata_0.25")
    if not os.path.exists("test_digital_txt/traindata_0.75"):
        os.mkdir("train_digital_txt/traindata_0.75")
    for k in range(0,10):
        nums = os.listdir("train_digital_txt/%s" %k)
        for i in range(0,660): # 复制训练样本
            shutil.copyfile("train_digital_txt/%s/%s_%s.txt"  %(k,k,i),"train_digital_txt/traindata_0.75/%s_%s.txt"  %(k,i) )
        for i in range(660,880): # 复制测试样本
            shutil.copyfile("train_digital_txt/%s/%s_%s.txt"  %(k,k,i),"test_digital_txt/testdata_0.25/%s_%s.txt"  %(k,i) )
accuracy_rating_classify()
            
