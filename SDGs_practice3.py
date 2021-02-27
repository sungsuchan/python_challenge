## index 다루기. 

import pandas as pd

"df = pd.DataFrame([[90,98,85,100],[80,89,95,90],[70,95,100,90]],
                  index = ['서준', '우현', '인아'],
                  columns = ['수학','영어','음악','체육'])"

# set_index('열이름') : 기존 index는 삭제됨.

df.index
df.sort_index()
df.set_index("수학", inplace=True) # 열에 있는 것을 index로 가져옴.
df
df.sort_index()
df.set_index(["영어","음악"])



# reset_index() : 초기화, 기존 index는 열의 자리에 위치하게됨.

df.reset_index()
df = df.reset_index()
df
df.rename(columns = {"index":"name"})

df.set_index("index")



# index 값 수정하기.

df.index[0] = '준서' # error, 한 개만 수정할 수 없다.
df.index = ['준서','우현','인아']
df




# reindex()

df.reindex(['우현','서준','인아'])
df.reindex(['우현','서준','인아','철수'])
df.reindex(['우현','서준','인아','철수'], fill_value = 80)
df.reindex(['우현','서준','인아','철수'], method = 'ffill')



# data.xlsx 불러오기.

df= pd.read_excel("data.xlsx")



## Q. 몇 행 몇 열인가?
df.info()
df.index

## Q. AGE열을 index로 만들어주세요.
df.set_index("AGE",inplace = True)
df

## Q. 나이순으로 가지런하게 만들어서 저장하라.
df = df.sort_index()

## Q. 새로운 index를 만들고 AGE는 열로 보내기
df = df.reset_index()
df

pd.read_excel("data.xlsx",index_col="AGE").sort_index().reset_index()






# 데이터프레임 살펴보기 : 

import seaborn as sns

df = sns.load_dataset('titanic')
df

df.head()
df.tail(3)
df.columns
df.index
df.info()
df.describe()
df[['age','fare']].describe()
df.count() 
df[['age','fare']].count()
df[['survived']].value_counts() # R에서의 table과 유사.


df['age'].value_counts()
df[['pclass','age']].value_counts()
df.columns
df.sex.value_counts()
df.embark_town.unique() # array가 출력됨.

df.columns


## Q. age, fare만 뽑아서 앞에 5개와 그 후 5개를 각각 저장하기.

df1 = df[['age','fare']].head(5)
df1 = df[['age','fare']].iloc[0:5]
df2 = df[['age','fare']].iloc[5:10]
df2
df1

## Q. df1과 df2를 더하는 방법?

df1 + 10
df1 + df2

df2 = df2.reset_index().drop('index',axis=1)
df2 = df2[['age','fare']]
df2

df1 + df2

## Q. 1등급칸, 2등급칸, 3등급칸은 몇명인가?

df.pclass.value_counts().sort_index()




# 통계값 구하기.

df['fare'].describe()
df[['age','fare']].mean() # NA는 무시하고 계산함.
df[['pclass','fare']].corr()



# groupby()

df['class']
df.pclass

df = df[['class','age','fare','survived']]
df.loc[:,['class','age','fare','survived']]

df.groupby('class')[['fare','age']].max()
df

df.groupby('survived')['fare'].max()

df.groupby('class').mean().iloc[2]

df.groupby('class').get_group('Third').mean()

df.groupby('class')['fare'].get_group('Third').mean()





