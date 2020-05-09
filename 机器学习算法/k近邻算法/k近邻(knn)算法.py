from numpy import np
import operator
# 从列方向扩张  tile(字典,(列数,1))
# 从行方向扩张  tile(字典,(行数,0))
def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0]  #  扩展行数，测试集行数与训练集行数一样
    dif = tile(testdata, (traindatasize, 1)) # why 行数一致，是否确保所有训练集都与测试集计算
    sqdif = dif**2 #  差值平方
    sumsqdif = sqdif.sum(axif=1) #  平方求和，求出距离的平方
    distance = sumsqdif**0.5 #  开方，求出距离
    sortdistance = distance.argsort() # 距离升序
    count = {}
    for i in range(0,k):
        vote = labels[soutdistance[i]]
        count[vote] = count.get(vote,0) + 1  #  类别次数+1
    sortcount = sorted(count.items(),key=operator.itemgetter(1),reverse=True) # reverse降序,不懂
    return sortcount[0][0]  # 返回分类结果
