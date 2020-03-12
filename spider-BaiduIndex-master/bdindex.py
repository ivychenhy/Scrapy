import requests,json,time

def get_index(keyword,cook):
    headers={
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
         'Cookie': cook,
        'Host': 'index.baidu.com',
        'Referer': 'http://index.baidu.com/v2/main/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    #keyword="seo"
    url=f'http://index.baidu.com/api/SearchApi/index?word={keyword}&area=0&days=30'
    response=requests.get(url,headers=headers).text
    time.sleep(2)
    #req=requests.get(url,headers=headers).json() #转换为json
    req=json.loads(response) #转换为json
    print(req)
    print(req['data']['generalRatio'][0])
    for k,v in req['data']['generalRatio'][0].items():
        print(k,v)

    data=req['data']['generalRatio'][0]
    all_avg=data['all']['avg']  #百度指数
    pc_avg=data['pc']['avg']  #百度pc端指数
    wise_avg=data['wise']['avg']  #百度移动端指数
    print(f'百度指数:{all_avg}')
    print(f'百度指数:{pc_avg}')
    print(f'百度指数:{wise_avg}')



if __name__ == '__main__':
    keyword=input('请输入要查询百度指数的关键词：')
    cook =input('请添加百度账号的cookies：')
    get_index(keyword, cook)
