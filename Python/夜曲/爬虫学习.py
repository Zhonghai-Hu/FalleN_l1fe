# 导入requests模块
import requests
from bs4 import BeautifulSoup

url = "https://nocturne-spider.baicizhan.com/2020/08/07/1/"
# requests.get()是获取网页信息的主要函数
response = requests.get(url)
# Response [200]表示此次浏览器的请求执行成功
print(response)
# 使用.status_code属性获取状态码，并赋值给statusCode
statusCode = response.status_code

if statusCode == 200:
    # 使用.text属性获取网页前1000个字符的内容
    html = response.text
    print(html)
    # BeautifulSoup() 函数可以把不标准的 HTML 代码重新进行了自动更正
    soup = BeautifulSoup(html, "lxml")
    """print(soup)"""
    # find_all() 函数可以查询 soup 中所有符合条件的元素，组成一个列表
    # find_all(name="标签") 根据标签名查询节点
    ps = soup.find_all(name = "p")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    for content in ps:
        contentString = content.string
        contenttext = content.text
        print(contentString)
        print("-------------------------------------------------------------")
        print(contentText)
else:
    print("请求数据失败")