def QR_Code(): # 二维码.jpg 转换成txt文本
    from PIL import Image
    fh = open("二维码/二维码.txt","a")  # 打开txt文本
    im = Image.open("二维码/二维码.jpg") # 打开二维码图片
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
QR_Code()
