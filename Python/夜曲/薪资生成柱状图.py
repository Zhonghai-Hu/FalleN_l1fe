from pyecharts.charts import Bar

with open(r"C:\Users\FalleN_l1fe\Documents\GitHub\FalleN_l1fe\Python\夜曲\职业数据.txt", "r") as f:
    # readlines() 函数可以读取 txt 文件中的所有行并返回一个列表
    dataList = f.readlines()
    # print(dataList)
cityDict = {}

for data in dataList:
    if "薪资面议" in data or "面议" in data:
        continue

    city = data.split(",")[2]
    salary = data.split(",")[3]
    daily = salary.split("/")[0]

    if len(daily.split("-")) == 2:
        start = daily.split("-")[0]
        end = daily.split("-")[1]
        average = (int(start)+int(end))/2
    else:
        average = int(daily)

    if city not in cityDict.keys():
        cityDict[city] = []

    cityDict[city].append(average)

city_num_dict = {}
#items() 函数把字典中每对 key 和 value 组成一个元组 ，并把这些元组放在列表中返回
for key, value in cityDict.items():
    average_value = sum(value)//len(value)
    cityDict[key] = average_value
    city_num_dict[key] = len(value)

bar = Bar()
bar.add_xaxis(list(cityDict.keys()))
bar.add_yaxis("各城市薪资", list(cityDict.values()))
bar.render(r"C:\Users\FalleN_l1fe\Documents\GitHub\FalleN_l1fe\HTML\salary.html")

bar_city = Bar()
bar_city.add_xaxis(list(city_num_dict.keys()))
bar_city.add_yaxis("职位数量",list(city_num_dict.values()))
bar_city.render(r"C:\Users\FalleN_l1fe\Documents\GitHub\FalleN_l1fe\HTML\positions.html")