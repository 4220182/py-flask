import pandas as pd
import numpy as np

logs = []
with open('./logs/users.log') as f:
    for line in f:
        logs.append(line.strip())

l = pd.DataFrame({'message': logs})

l1 = l['message'].str.split(' : ',expand = True)
l1.columns=['步骤名称','c1','任务项','状态']

l2 = l1.join(l)

l3 = l2['状态'].str.split('(',expand=True)
l3.columns=['完成状态','时间']
l3['时间'] = l3['时间'].str.replace(')','')

l3['时间'] = pd.to_datetime(l3['时间'])

l4 = l3.join(l2)[['步骤名称','任务项','完成状态','时间']]
l4.index.name='执行顺序'

l5 = l4.groupby(['步骤名称','任务项'])['时间'].agg([np.min, np.max]).rename(columns={'amin':'开始时间','amax':'结束时间'}).reset_index()

l5['耗时(分钟)'] = (l5['结束时间'] - l5['开始时间']).dt.seconds/60

print(l5[['步骤名称','开始时间','结束时间']])
