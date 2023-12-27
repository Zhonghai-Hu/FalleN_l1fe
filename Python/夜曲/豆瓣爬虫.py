import requests
from bs4 import BeautifulSoup
import jieba
from pyecharts.charts import WordCloud
from collections.abc import Iterable

#豆瓣评论网址
url = "https://movie.douban.com/subject/2129039/comments?sort=new_score&status=P"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response = requests.get(url, headers = headers)
StatusCode = response.status_code

wordlist = []
letter = {}
if StatusCode == 200:
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    content_all = soup.find_all(class_="short")
    for content in content_all:
        contentString = content.string
        words = jieba.lcut(contentString)
        wordlist += words
        for word in wordlist:
            if len(word) > 1:
                if word not in letter.keys():
                    letter[word] = 1
                else:
                    letter[word] += 1
        print(letter)
    wd = WordCloud()
    #series_name 为必须参数，就是必须传入，词云图中展示的是文字内容
    #data_pair 参数是指传入词云图中的数据
    # items() 函数，将字典 wordDict中的每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
    #word_size_range 是用来设置词云图中字体大小范围，它的数据类型是列表
    wd.add(series_name = "", data_pair= letter.items(), word_size_range = [20,80])
    wd.render(r"C:\Users\letiao\Documents\GitHub\FalleN_l1fe\HTML\picture.html")
    print("success")