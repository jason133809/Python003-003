#auth:donghui.li
#date:20200825
#comment:用requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"

headers={'user-agent':user_agent}

myurl="https://maoyan.com/films?showType=3"



response=requests.get(myurl,headers=headers)

bs_info= bs(response.text,'html.parser')



items=bs_info.select('.movie-hover-info',limit=10)



l=[]
list1=[]
list2=[]
for item in items:
        #print(item)
    movie_tital=item.select('.movie-hover-title')[0].find('span',attrs={'class':'name'}).get_text()
    movie_attrs=item.select('.movie-hover-title')[1].get_text().replace("\n", "").strip(" ")
    movie_time=item.select('.movie-hover-title')[3].get_text().replace("\n", "").strip(" ")
    data=movie_tital.strip()
    data1=movie_attrs.replace('类型:','').strip()
    data2=movie_time.replace('上映时间:','').strip()
    l.append(data)
    list1.append(data1)
    list2.append(data2)


vdata={'tital':l,'attrs':list1,'relasetime':list2}

df=pd.DataFrame(vdata)

df.to_csv('D:\\maoyan.csv',encoding='utf_8_sig')
