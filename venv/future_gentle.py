import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Host': 'www.cfachina.org'}
name = []
gender = []
congye1= []
congye2 = []
department = []
title = []
time = []
for i in range(1,45 ):
    link = 'http://www.cfachina.org/cfainfo/organbaseinfoOneServlet?organid=+G01095+&currentPage=' + str(i)+'&pageSize=20&selectType=personinfo&all=undefined'
    r = requests.get(link, headers=headers, timeout=20)
    print(str(i + 1), '页响应状态码：', r.status_code)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    # print('soup:', soup)
    #for j in range(0,20)
    div_list = soup.find_all('tr')
    # print('div_list:', div_list)
    tds_list = []

    for each in div_list:
        tds = each('td')
        j = 0
        for row in tds:
            #print(row)
            text = ''.join(row.findAll(text=True))
            j = j+1
            if j ==1:
                name.append(text)
            if j ==2:
                gender.append(text)
            if j ==3:
                congye1.append(text)
            if j ==4:
                congye2.append(text)
            if j ==5:
                department.append(text)
            if j ==6:
                title.append(text)
            if j ==7:
                time.append(text)
            #tds_list.append(text)
df={"name" : name,
    "gender" : gender,
    "congye1": congye1,
    "congye2": congye2,
    "department" : department,
    "title" : title,
    "time": time
    }
td_df=pd.DataFrame(df)
td_df.to_csv('D:/爬虫/yonganfuture.csv',encoding="utf_8_sig")
'''

td_df = pd.DataFrame('姓名': fef,
                     '性别':dfs,
                     '从业资格号': fef,
                     '投资咨询从业证书号': dfs,
                     '任职部门': fef,
                     '职务': dfs,
                     '任现职时间': dfs)
'''

