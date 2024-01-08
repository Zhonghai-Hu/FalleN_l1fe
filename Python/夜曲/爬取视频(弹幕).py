import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line

# "https://comment.bilibili.com/{cid}.xml"
url = "https://comment.bilibili.com/218710655.xml"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
response = requests.get(url, headers=headers)
#  .encoding 属性可以找出 requests 模块使用了什么编码。
# print(response.encoding)
#  .apparent_encoding 属性会从网页的内容中分析网页编码的方式。
# print(response.apparent_encoding)
response.encoding = response.apparent_encoding
xml = response.text
soup = BeautifulSoup(xml,"lxml")
content_all = soup.find_all(name = "d")
# print(content_all)

timeList = []
for video in content_all:
    data = video.attrs["p"]
    time = data.split(",")[0]
    timeList.append(float(time))
# print(timeList)


subtitlesDict = {}
for x in range(25):
    start = 30*x+1
    end = 30*(x+1)
    segment_range = f"{start}-{end}"
    subtitlesDict[segment_range] = 0

for subtitle in subtitlesDict.keys():
    start_key = subtitle.split("-")[0]
    end_key = subtitle.split("-")[1]

    for item in timeList:
        if int(start_key)<= item <= int(end_key):
            subtitlesDict[subtitle] = subtitlesDict[subtitle] + 1
# print(subtitlesDict)

line = Line()
line.add_xaxis(list(subtitlesDict.keys()))
line.add_yaxis("弹幕统计", list(subtitlesDict.values()))
line.render(r"C:\Users\FalleN_l1fe\Documents\GitHub\FalleN_l1fe\HTML\line.html")
print("success")