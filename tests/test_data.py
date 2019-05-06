import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
import csv

#从url获取数据
def getSinglePage(page):
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (str(page))
    tb = pd.read_html(url, skiprows=[0 ,1])[0]  # 跳过前两行
    return tb.drop([len(tb) - 1])  # 去掉最后一行

path_root='C:\\Users\\Administrator\\Desktop\\python\\Myproject\\报表.csv'
with open(path_root, 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['开奖日期', '期号', '中奖号码', '销售额元', '中奖注数一等奖', '中奖注数二等奖', '详细'])
    for i in range(1, 100):  # 目前100页数据

        getSinglePage(i).to_csv(path_root, mode='a', encoding='utf_8_sig', header=0, index=0)


#转化为DataFrame
csv_data=pd.read_csv(path_root)
df=pd.DataFrame(csv_data)
#筛选数据
