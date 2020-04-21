from  sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
def dictvec():
    """
    字典数据抽取
    :return: None
    """
    dict = DictVectorizer(sparse=False) # 实例化
    data  = dict.fit_transform([{'x':'a','y':100, 'z':22},{'x':'b','y':2, 'z':222},{'x':'c','y':22, 'z':1222}])
    print(dict.get_feature_names())
    print(dict.inverse_transform(data))
    print(data)
    return None

def countvec():
    """
    对文本进行特征值化
    :return: None
    """
    cv = CountVectorizer()
    # data = cv.fit_transform(["dd a d a ss ss d d","adfad adsfads"])
    data = cv.fit_transform(["Hello! Good evening. I am studying Python.","Good man can use Python."]) #  单个汉字不统计
    print(cv.get_feature_names() ) # 统计所有文章当中所有的词，重复的只看做一次
    print(data.toarray())  #  对每篇文章，在词的列表里面进行统计每个词出现的次数
    # 单个字母不统计：没有分类依据
    return  None

def cutword():
    """
    切分词
    :return: None
    """
    con1 = jieba.cut("早上好，我在学Python。")
    con2 = jieba.cut("您好，我不会用Python。")
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    # 把列表转换为字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    return c1, c2

def chinesevec():
    """
    中文特征值化
    :return: None
    """
    c1, c2 = cutword()  #  获取句子分词
    cv = CountVectorizer()
    # data = cv.fit_transform(["dd a d a ss ss d d","adfad adsfads"])
    data = cv.fit_transform([c1, c2])  # 单个汉字不统计
    print(cv.get_feature_names())  # 统计所有文章当中所有的词，重复的只看做一次
    print(data.toarray())  # 对每篇文章，在词的列表里面进行统计每个词出现的次数

    # 准备句子，利用jieba.cut进行分词
    # 实例化CountVectorizer
    # 讲分词结果变成字符串当做fit_transform的输入值
    return None

if __name__ == '__main__':
    # dictvec()
    countvec()
    chinesevec()