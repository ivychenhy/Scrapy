from get_index import BaiduIndex
from get_feedindex import BaiduFeedIndex
from get_newsindex import BaiduNewsIndex
import pandas as pd


def dict_to_df(d):
    df = pd.DataFrame(d.items())
    df.set_index(0, inplace=True)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    return df

def getIndex(keywords,endDate):
    baidu_index = BaiduIndex(keywords, '2015-01-01', endDate)
    df = pd.DataFrame()
    for index in baidu_index.get_index():
        #print(index)
        baidu_index2 = dict_to_df(index)
        if baidu_index2['type']=='all':
            if df.empty:
                df = baidu_index2
            else:
                df = df.append(baidu_index2)
    df.to_csv('D:/coin/spider-BaiduIndex-master/spider-BaiduIndex-master/SearchIndex.csv',encoding='utf_8_sig')

def getFeedIndex(keywords,endDate):
    baidu_index = BaiduFeedIndex(keywords, '2017-07-03', endDate)
    df = pd.DataFrame()
    for index in baidu_index.get_index():
        #print(index)
        baidu_index2 = dict_to_df(index)
        if df.empty:
            df = baidu_index2
        else:
            df = df.append(baidu_index2)
    df.to_csv('D:/coin/spider-BaiduIndex-master/spider-BaiduIndex-master/FeedIndex.csv',encoding='utf_8_sig')

def getNewsIndex(keywords,endDate):
    baidu_index = BaiduNewsIndex(keywords, '2015-01-01', endDate)
    df = pd.DataFrame()
    for index in baidu_index.get_index():
        #print(index)
        baidu_index2 = dict_to_df(index)
        if df.empty:
            df = baidu_index2
        else:
            df = df.append(baidu_index2)
    df.to_csv('D:/coin/spider-BaiduIndex-master/spider-BaiduIndex-master/NewsIndex.csv',encoding='utf_8_sig')

if __name__ == "__main__":
    keywords = ['比特币']
    endDate = '2020-01-01'
    getNewsIndex(keywords, endDate)




