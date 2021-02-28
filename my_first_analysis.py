## 근 3년간 20대 청년이 사망한 주요 원인에 대한 분석


### 데이터 로딩 밑 처리

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family = 'AppleGothic')


df = pd.read_excel("사망원인.xlsx")
df.info()
df.index


df.set_index("연령(5세)별", inplace = True)

df.drop(['2017','2018','2019'], axis = 1, inplace = True)
df.loc[:,'사망원인별(103항목)'].value_counts()

df.loc[:,'사망원인별(103항목)']

df['사망원인별(103항목)']

df.dropna().loc[:,'사망원인별(103항목)']




df.fillna(method = 'ffill', inplace = True)
df.columns


df1 = df.loc[['20 - 24세','25 - 29세']]
df1.rename(columns = {'2017.1' : '2017','2018.1' : '2018','2019.1' : '2019'},inplace = True)
df1.replace('-',np.nan,inplace = True)



df1['상승추이'] = df1['2019'] - df1['2017']
df1.sort_values(by = '상승추이', axis = 0 , ascending=False)
df2 = df1.sort_values(by = '상승추이',axis =0).groupby(['사망원인별(103항목)','성별']).mean()

df3 = df2.reset_index()
df3.iloc[0:60:3].sort_values('상승추이',axis =0,ascending = False)
df4 = df3.set_index('사망원인별(103항목)').loc[['질병이환 및 사망의 외인 (V01-Y89)','달리 분류되지 않은 증상, 징후 (R00-R99)','신생물 (C00-D48)']]
df4.rename(columns={'2017':2017,'2018':2018,'2019':2019},inplace =True)

df4.drop('상승추이',axis =1, inplace = True)


type(df4['성별'])

df4.reset_index(inplace = True)
df4.drop([0,3,6],axis=0, inplace =True)
df4 = pd.concat([df4]*3).sort_index()

df4 = df4.reset_index().drop('index',axis =1)
df4.iloc[1,2] = 32.55
df4.iloc[2:,2].replace([33.65],31.10,inplace =True)
df4.iloc[4:6,2] = [16.70,19.60]
df4.iloc[7:9,2] = [2.20,2.30]
df4.iloc[10:12,2] = [1.15,1.45]
df4.iloc[13:15,2] = [3.90,4.70]
df4.iloc[16:18,2] = [4.30,3.90]

df4.rename(columns = {2017:'사망률'},inplace =True)
df4.drop([2018,2019],axis=1,inplace = True)

date = []
for i in df4.index:
    if i % 3 == 0 :
        date.append(2017)
    elif i % 3 == 1 :
        date.append(2018)
    else :
        date.append(2019)
df4["Year"] = date




df7 = df4.iloc[0:6] # 질병이환 및 사망의 외인 (V01-Y89)
df8 = df4.iloc[6:12] # 달리 분류되지 않은 증상, 징후 (R00-R99)
df9 = df4.iloc[12:] # 신생물 (C00-D48)



### 데이터 시각화.

font2 = {'family': 'Times New Roman',
      'color':  'blue',
      'weight': 'bold',
      'size': 12}

xticks = [i if i % 1 == 0 else "" for i in range(2017, 2020)]
plt.rcParams["figure.figsize"] = (14,10)
plt.tight_layout()

plt.subplot(2,2,1)
plt.axis([2017,2019,14,40])  #plt.xlim(), plt.ylim()
plt.xlabel('Year')
plt.ylabel('사망률(10만명당)')
plt.text(2018, 35, '질병이환 및 사망의 외인 (V01-Y89)')
plt.text(2017, 41, 'TOP3 Death Rate Trend By Cause Of Death', fontsize = 13,fontdict=font2)
plt.xticks(np.arange(2017,2020,1), labels = xticks, fontsize = 9)

sex = list(set(df7['성별']))
for i in sex:
    plt.plot(df7[df7['성별']==i].Year, df7[df7['성별']==i]['사망률'], label = i, alpha = 0.6)

plt.legend(loc = 'upper left', ncol = 2, fontsize = 'x-small', framealpha = 0.4) 


plt.subplot(2,2,2)
plt.axis([2017,2019,0,2.5])  #plt.xlim(), plt.ylim()
plt.xlabel('Year')
plt.ylabel('사망률(10만명당)')
plt.text(2017.8, 1.75, '달리 분류되지 않은 증상, 징후 (R00-R99)')
plt.xticks(np.arange(2017,2020,1), labels = xticks, fontsize = 9)
sex = list(set(df8['성별']))
for i in sex:
    plt.plot(df8[df8['성별']==i].Year, df8[df8['성별']==i]['사망률'], label = i, alpha = 0.6)

plt.legend(loc = 'upper left', ncol = 2, fontsize = 'x-small', framealpha = 0.4) 


plt.subplot(2,2,3)
plt.axis([2017,2019,3.8,5])  #plt.xlim(), plt.ylim()
plt.xlabel('Year')
plt.ylabel('사망률(10만명당)')
plt.text(2017.8, 4.5, '신생물 (C00-D48)')
plt.xticks(np.arange(2017,2020,1), labels = xticks, fontsize = 9)
sex = list(set(df9['성별']))
for i in sex:
    plt.plot(df9[df9['성별']==i].Year, df9[df9['성별']==i]['사망률'], label = i, alpha = 0.6)

plt.legend(loc = 'upper left', ncol = 2, fontsize = 'x-small', framealpha = 0.4) 




