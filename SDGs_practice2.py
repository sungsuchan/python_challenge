# 데이터프레임 연습 2.

# Q) 데이터 프레임을 만들어주세요.
import pandas as pd
import plotly.express as px


df = pd.DataFrame([[90,98,85,100],[80,89,95,90],[70,95,100,90]],
                  index = ['서준', '우현', '인아'],
                  columns = ['수학','영어','음악','체육'])

df

df = px.data.gapminder()
df.info()

df




# 행과 열 추가하기.

df.loc['상기'] = [95,100,80,95]
df

df.loc[:,'미술'] = [80,90,95,100]
df['미술'] = [80,90,95,100]
df

type(df['미술']) # 이건 시리즈 

type(df[['체육','미술']])

type(df[['미술']]) # 데이터 프레임 한줄로 뽑기

df['과학'] = 80 # 같은 값 추가하기.
df




# 값 수정하기.

df.iloc[0,0] = 95 # 서준이 수학 점수 바꾸기.
df



# 정렬하기.

df.sort_index()
df.sort_values(by = '수학',axis=0,ascending=False)



# chropleth (단계구분도)

## conda install folium

import pandas as pd
import folium 
import json
import os



# working directory 확인하고 바꾸기.

os.getcwd()
os.chdir() # /는 \\와 같다.



# excel 파일 읽기.

file_path = "./경기도인구데이터.xlsx"
df = pd.read_excel(file_path)
df.columns
df.index
df
df = pd.read_excel(file_path, index_col = "구분")
df
df.info()
df.head(3)
df[2007] = df[2007].astype(str)




# 열의 데이터형태 바꾸기.

a=[1,2,3]
type(a)
a = str(a) # 우리는 따로따로 만들고 싶다!
a= map(str,a) # map을 활용!
a = list(map(str,a))
a = list(map(int,a)) # 다시 원래대로!

df.columns
df.columns = list(map(str,df.columns))
df.columns = df.columns.map(str)
df.columns = df.columns.map(int)
df.columns = df.columns.astype(str) # astype은 시리즈와 데이터프레임형태만 가능.
df['2007'] = df['2007'].astype(int)
df.columns
df['2007']

for i in df.columns:
    df[i] = df[i].astype(str)  # for문을 활용한 모든 데이터셋 바꾸기!(중요!!₩)




# 람다 함수.

list(map(lambda a: a*2,a))
data = list(range(1,11))
list(map(lambda a:a*2,data))
list(filter(lambda a: a %2 == 0, data))





# json 파일 읽기.

with open("./경기도행정구역경계.json", encoding ='utf-8') as f:
    geo_data =json.load(f)
    
    
    

# 서울 지도 불러오기.

g_map = folium.Map(location = [37.55,126.90], tile = "Starmen WaterColor",zoom_start=9)
g_map.save("g_map.html")




# 단계구분도 그리기.

folium.Choropleth(geo_data = geo_data,
                  data = df,
                  columns = (df.index,"2007"),
                  key_on = 'feature.properties.name').add_to(g_map)
g_map.save("g_map1.html")


df[['구분',2007]]


















