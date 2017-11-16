## pandas
### pandas常用基本函数
```python
unique()
isin()
isnull()
notnull()
date_range()
sort_index()
dropna()
fillna()
value_counts()
concat()
duplicated()
drop()
apply()
```
###  pandas数据处理
#### 数据处理
- 加载
- 组装
  - 合并 `pandas.merge()`
  - 拼接 `concat()`
  - 组合 `combine_first()`
- 变形
- 删除`del drop() `
#### 数据转换
``` python
#删除重复元素
duplicated()
drop_duplicates()
#映射
replace()
map()
rename()
```
#### 数据聚合
 `groupby()`

---
## matplotlib
### 基础操作
```python
import matplotlib.pyplot as plt

# 标题
plt.title("my first plot",fontsize=20, fontname='Times New Roman')
# 坐标轴标题
plt.xlabel('counting',color='gray',fontsize=15)
plt.ylabel('square values',color = 'gray')
# 坐标范围
plt.axis([0,5,0,20])
# 插入文本
plt.text(1,1.5,'first')
plt.text(2,4.5,'second')
plt.text(1.1,12,r'$y=x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
# 网格线
plt.grid(True)
# 作图
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
# 图例
plt.legend(['First series','second series','third series'],loc=2)
# 保存图片
plt.savefig('my_chart.png')
# show
plt.show()
```
### 图标类型
#### 线形图
##### 普通线形图
```python
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,'k--',linewidth=3)
plt.plot(x,y2,'m-.')
plt.plot(x,y3,color='#87a3cc',linestyle='--')
# 替换刻度线
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$\pi$',r'$0$',r'$\pi$',r'$2\pi$'])
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.show() 
```
##### 坐标轴远点位于（0,0）的线形图
```python
#线形图
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,'b')
plt.plot(x,y2,'r')
plt.plot(x,y3, 'g')
# 替换刻度线
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$\pi$',r'$0$',r'$\pi$',r'$2\pi$'])
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
# 用注释和箭头标明某个点
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}= 1$',xy=[0,1],xycoords='data',xytext=[30,30],
             fontsize=16,textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle ='arc3,rad=.2'))
#移动坐标轴原点
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
```
#### 直方图
```python
import numpy as np
import matplotlib.pyplot as plt

pop = np.random.randint(0,100,100)
n, bins, patches = plt.hist(pop, bins=20)
plt.show()
```
#### 条状图
```python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values = [5,7,3,4,6]
std1 = [0.8,1,0.4,0.9,1.3]
plt.title('A bar chart')
# 带有误差线的条状图
plt.bar(index,values,yerr=std1,error_kw={'error':'0.1','capsize':6},alpha=0.7,label='First')
plt.xticks(index,['A','B','C','D','E'])
plt.legend(loc=2)
plt.show()
```
##### 水平条状图
```python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values = [5,7,3,4,6]
std1 = [0.8,1,0.4,0.9,1.3]
plt.title('A Horizontal bar chart')
plt.barh(index,values,xerr=std1,error_kw={'error':'0.1','capsize':6},alpha=0.7,label='First')
plt.yticks(index,['A','B','C','D','E'])
plt.legend(loc=5)
plt.show()
```
##### 多序列条状图
```python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,6,4,5,7]
values3 = [5,6,5,4,6]
bw = 0.3
plt.axis([0,5,0,8])
plt.title('A Multiseries bar chart',fontsize=20)
plt.bar(index,values1,bw,color='b')
plt.bar(index+bw,values2,bw,color='g')
plt.bar(index+bw*2,values3,bw,color='r')
plt.xticks(index+bw,['A','B','C','D','E'])
plt.show()
```
##### 多序列水平条状图
``` python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,6,4,5,7]
values3 = [5,6,5,4,6]
bw = 0.3
plt.axis([0,5,0,8])
plt.title('A Multiseries bar chart',fontsize=20)
plt.bar(index,values1,bw,color='b')
plt.bar(index+bw,values2,bw,color='g')
plt.bar(index+bw*2,values3,bw,color='r')
plt.xticks(index+bw,['A','B','C','D','E'])
plt.show()
```
##### 多序列堆积条状图
``` python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values1 = np.array([5,7,3,4,6])
values2 = np.array([6,6,4,5,7])
values3 = np.array([5,6,5,4,6])
plt.axis([-0.5,5,0,20])
plt.title('A Multiseries  Stacked bar chart',fontsize=20)
plt.bar(index,values1,color='b')
plt.bar(index,values2,color='g',bottom=values1)
plt.bar(index,values3,color='r',bottom=(values1+values2))
plt.xticks(index,['A','B','C','D','E'])
plt.show()
```
##### 多序列水平堆积条状图
``` python
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
values1 = np.array([5,7,3,4,6])
values2 = np.array([6,6,4,5,7])
values3 = np.array([5,6,5,4,6])
plt.axis([0,20,-0.5,5])
plt.title('A Multiseries Horizontal Stacked bar chart',fontsize=15)
plt.barh(index,values1,color='b')
plt.barh(index,values2,color='g',left=values1)
plt.barh(index,values3,color='r',left=(values1+values2))
plt.yticks(index,['A','B','C','D','E'])
plt.show()
#设置同种颜色，不同影线填充条状图
plt.barh(index,values1,color='w',hatch='xx')
plt.barh(index,values2,color='w',hatch='///',left=values1)
plt.barh(index,values3,color='w',hatch='\\\\',left=(values1+values2))
```
#### 饼图
``` python
import matplotlib.pyplot as plt

labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,45,15]
colors = ['yellow','green','red','blue']
explode = [0.3,0,0,0]
plt.title('A Pie chart')
plt.pie(values,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',startangle=180)
plt.axis('equal')
plt.show()
```
