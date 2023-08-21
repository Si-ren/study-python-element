# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:54:04 2022

@author: A@超
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import warnings
# 忽略警告
warnings.filterwarnings("ignore")

# 1 读取文件
df = pd.read_excel("双十一淘宝美妆数据.xlsx")

#  商品总数
goods_total = len(df.id.unique())

# 品牌总数
brand_total = len(df['店名'].unique())

print("数据中商品总数为{},品牌总数为{}".format(goods_total, brand_total))

# ② 双十一当天在售的商品占比情况
df['day'] = df['update_time'].dt.day

# 双11商品
data_11 = df[df['day'] == 11]
# 双11商品个数
data_11_goods_num = len(data_11["id"].unique())

print("双11商品个数为{}, 占比为{:.2%}".format(data_11_goods_num, data_11_goods_num/goods_total))

'''

    按照商品销售情况分类
    # 如何判断产品在双11之前  双11当前 双11 之后进行销售
    day: min  max   
    新增一个在在双11 当天销售的字段
    a.按照day进行统计操作. 分析id 最小销售日期和最大销售日期
    b.确定那些商品在"11号当天进行销售"
    id ,min,max,11号当天进行销售,type
    
'''
day_group = df[['id','day']].groupby(('id')).agg(['min','max'])['day']
# 将day_group索引重置
day_group.reset_index(inplace=True)

# 生成双11在售商品的数据
new_data_11 = pd.DataFrame({"id":data_11["id"].unique(),"双11售卖":True})

# 按天分组后的数据和仅仅是双11销售的产品进行关联
day_group = pd.merge(day_group,new_data_11,on="id",how="left")
day_group['双11售卖'] = day_group['双11售卖'].fillna(False)

# 对数据进行分类

day_group['type'] = "分类"
# A. 11.11前后及当天都在售 → 一直在售
day_group['type'][(day_group['min'] < 11) & (day_group['max'] > 11) & (day_group['双11售卖']==True)]='A'
#B. 11.11之后停止销售 → 双十一后停止销售 ,<=11 
day_group['type'][(day_group['min'] < 11) & (day_group['max'] == 11)] = 'B'
#day_group['type'][(day_group['min'] < 11) & (day_group['双11售卖']==True)] = 'B'
day_group['type'][(day_group['min'] < 11) & (day_group['max'] == 11)] = 'B'
#C. 11.11开始销售并当天不停止 → 双十一当天上架并持续在售
day_group['type'][(day_group['min'] == 11) & (day_group['max'] > 11)]='C'

# D. 11.11开始销售且当天停止 → 仅双十一当天有售'
day_group['type'][(day_group['min'] == 11) & (day_group['max'] == 11)]='D'
# E. 11.5 - 11.10 → 双十一前停止销售
day_group['type'][day_group['max'] < 11]='E'

# F. 仅11.11当天停止销售 → 仅双十一当天停止销售
day_group['type'][(day_group['min'] < 11) & (day_group['max'] > 11)& (day_group['双11售卖']==False)]='F'

# G. 11.12开始销售 → 双十一后上架
day_group['type'][day_group['min'] > 11]='G'

# 绘制饼状图
day_group['type'].value_counts().plot.pie(autopct='%.2f%%',figsize=(10,10))



'''
    取出所有非双11 销售的商品
'''
data_not11 = day_group[day_group['双11售卖']==False]


# 所有F类型产品的
con1 = day_group[day_group['type'] == 'F']

# 查询所有 非双11 销售的商品中 预售的商品--

# 取出所有没有参数双11商品的原始数据
temp_data_not11 = pd.DataFrame({"id":data_not11["id"].values})

data_not11_source = pd.merge(temp_data_not11,df[['id',"title"]],on="id",how="left")

data_not11_sg= data_not11_source.groupby(['id','title']).count().reset_index()

pre_sale_data = data_not11_sg[data_not11_sg["title"].str.contains("预售")]

print("双11活动产品总个数为%s,包含预售商品%s个,包含双11活动商品%s个"%(len(pre_sale_data)+len(new_data_11),
                                              len(pre_sale_data),
                                              len(new_data_11)))


112  110 134   112  112  112


























