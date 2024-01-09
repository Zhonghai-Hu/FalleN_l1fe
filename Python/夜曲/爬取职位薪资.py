import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line
import time

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

def getPositionInfo(detail_url):
    response = requests.get(detail_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    job = soup.find(class_="new_job_name").find("span").string.strip()
    com_content = soup.find(class_="com_intro")
    companyName = com_content.find('a',class_="logo").find_next('a').text.strip()
    position = soup.find(class_="job_position").string.strip()

    salary = soup.find(class_="job_money cutom_font").string
    salary = salary.encode()
    salary = salary.replace(b"\xee\x8b\xbf", b"0")
    salary = salary.replace(b"\xee\xa2\x9c", b"1")
    salary = salary.replace(b"\xee\x90\xb7", b"2")
    salary = salary.decode()

    # print(f"{job},{companyName},{position},{salary}")
    with open(r"C:\Users\FalleN_l1fe\Documents\GitHub\FalleN_l1fe\Python\夜曲\职业数据.txt", "a") as f:
        f.write(job+","+companyName+","+position+","+salary+"\n")

for i in range(1,6):
    url = f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all(class_="title ellipsis font")

    for item in titles:
        detail_url = item.attrs["href"]
        getPositionInfo(detail_url)

    time.sleep(2)
    
print("success")