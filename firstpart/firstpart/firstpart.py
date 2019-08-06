import csv
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
#datapath='../../车险数据0802.csv'
datapath='./result.csv'
csv_f=pd.read_csv(datapath,engine='python',encoding='utf_8_sig')

#csv_file=csv.reader(open(datapath,'r'))
#X=[]
#for i in csv_file:
#    X.append(i)


def convert(s,csv_f):
    temp=pd.Categorical(csv_f[s])
    enc=OneHotEncoder()
    enc.fit(temp.codes.reshape(-1,1))
    ans=enc.transform(temp.codes.reshape(-1,1)).toarray()
    csv_f=csv_f.drop([s],axis=1)
    tempcolumns=[]
    for i in range(len(ans[0])):
        tempcolumns.append(s+'_'+str(i))
    csv_ans=pd.DataFrame(ans,columns=tempcolumns)
    df=pd.concat([csv_f,csv_ans],axis=1)
    #df.to_csv('result.csv',encoding='utf_8_sig')
    return df

df=convert('驱动类型',csv_f)
df.to_csv('result.csv',encoding='utf_8_sig')