#encoding=utf-8

import pandas as pd
import random as rd

#新建两个数据集
df=pd.DataFrame({
    "id":[rd.randrange(100,2000) for _ in range(100)],
    "name":["ldh"+str(rd.randrange(1,100)) for _ in range(100)],
    "age":[rd.randrange(20,60) for _ in range(100)],
    "sarary":[rd.randrange(2000,10000) for _ in range(100)]
})

df1=pd.DataFrame({
    "id":[rd.randrange(100,2000) for _ in range(100)],
    "name":["ldh"+str(rd.randrange(1,100)) for _ in range(100)],
    "age":[rd.randrange(20,60) for _ in range(100)],
    "sarary":[rd.randrange(2000,10000) for _ in range(100)]
})


#1.select * from t
print(df)

#2.select * from t limit 10
#print(df.head(10))

#3.select id from t
#print(df['id'])

#4.select count(1) from t
#print(df['id'].count())

#5.select * from t where id<1000 and age>30
#print(df[(df.id < 1000) & (df.age > 20)])
#print(df.query('id <1000 and age > 20'))

#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
#df6=df.groupby(['id'])['name'].apply(lambda  x:len(x.unique()))
#print(df6)
	
#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
#df7=pd.merge(df,df1,on='id',how="inner")
#print(df7)
 
	
#8. SELECT * FROM table1 UNION SELECT * FROM table2;
#df8= pd.concat([df,df1])
#print(df8)
 
	
#9. DELETE FROM table1 WHERE id=10;
#df9=df[(df['id']!=10)]
#print(df9)
	
#10. ALTER TABLE table1 DROP COLUMN column_name;
#df10=df.drop('id',axis=1)
#print(df10)