## 데이터프레임 만들기.

import pandas as pd

df = pd.DataFrame([[15, '남', '남중'],[17,'여','여중']],
                  index = ['철수','영희'],
                  columns = ['나이','성별','학교'])

df
print(df)
type(df)
dir(df)
df.index
df.columns


# Q) 데이터프레임 만들기
  수학  영어   음악   체육
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90

df = pd.DataFrame([[90,98,85,100],[80,89,95,90],[70,95,100,90]],
                  index = ['서준', '우현', '인아'],
                  columns = ['수학','영어','음악','체육'])
df
print(df)

# 행과 열 지우기.

df.drop('철수',axis =0)
df.drop('나이',axis =1)

df.drop(["나이",'성별'],axis=1, inplace = True)
df

# 행과 열 선택하기.

df = pd.DataFrame([[90,98,85,100],[80,89,95,90],[70,95,100,90]],
                  index = ['서준', '우현', '인아'],
                  columns = ['수학','영어','음악','체육'])
df

df.loc['서준'] # 행 선택시 .loc 사용.
df.loc['서준','인아'] # 에러가 난다.
df.loc[['서준','인아']] # 이렇게 해야한다.

df.iloc[0]
df.iloc[0,2] # 0행에 2열에 있는 값을 나타냄.
df.iloc[[0,2]]

df.iloc[0:2]
df.iloc[::2] # 시작 : 스탑 : 스텝.
df.iloc[::-1]

df['수학'] # 열은 default.
df[['수학','영어']]
df.수학 # 열은 .을 허용함.

# 행과 열의 이름 바꾸기(rename)
df

서준 -> 준서
df.rename(index = {'서준':'준서'})
df.rename(columns = {'수학':"math", "영어":"english"})

# Q)
import plotly.express as px
df = px.data.gapminder()
df
## 1. 열의 이름은 모두 무엇인가?
df.columns
## 2. country부터 gdpPercap까지의 열만 가져온 후 df로 저장하기.
df = df[['country','continent','year','lifeExp','pop','gdpPercap']]
df = df.iloc[:,0:6]
df = df.loc[:,'country':'gdpPercap']
## 3. index가 100, 200, 300, 400, 500을 각각 "A", "B", "C", "D", "E"로 바꾸기.
df.rename(index = {100 : "A", 200 :"B", 300:"C",400:"D",500:"E"},inplace=True)
## 4. "A", "B", "C", "D", "E"의 행을 가진 5행 6열인 df를 만들기
df.iloc[100:600:100]

# chropleth (단계구분도)

## conda install folium

import pandas as pd
import folium 
import json
import os

# working directory 확인하고 바꾸기.

os.getcwd()
os.chdir()

# excel 파일 읽기.

df = pd.read_excel("경기도인구데이터.xlsx")
df.columns
df.index

# json 파일 읽기.

with open("경기도행정구역경계.json", encoding ='utf-8') as f:
    geo_data =json.load(f)

# 서울 지도 불러오기.

g_map = folium.Map(location = [37.55,126.90], zoom_start=9)
g_map.save("g_map.html")

# 단계구분도 그리기.

folium.Choropleth(geo_data = geo_data,
                  data = df,
                  columns = ("구분",2007),
                  key_on = 'feature.properties.name').add_to(g_map)
g_map.save("g_map1.html")

df[['구분',2007]]


















