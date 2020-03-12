import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host': 'movie.douban.com'}
    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' +str(i*25)
        r = requests.get(link,headers = headers,timeout = 20)
        print(str(i+1),'页响应状态码：',r.status_code)
        #print(r.text)
        soup = BeautifulSoup(r.text,'lxml')
        #print('soup:', soup)
        div_list = soup.find_all('div',class_='hd')
        #print('div_list:', div_list)
        for each in div_list:
            movie = each.a.span.text.strip()
            #print('movie:',movie)
            movie_list.append(movie)
    return movie_list


movies = get_movies()
print(movies)

