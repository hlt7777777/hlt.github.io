## Naive Bayes (朴素贝叶斯)
---
### 原理
1. 先验概率
1. 条件概率
1. 贝叶斯定理
1. 极大似然估计
### 三种常见的贝叶斯分类器
#### 一、GuassianNB (高斯贝叶斯分类器)
**class sklearn.naive_bayes.GaussianNB**
1. 它假设特征的条件概率分布满足高斯分布
1. **无参数**
1. 属性
1. 方法：`fit()` `predict()` `score()` `partial_fit()`
#### 二、MultinomialNB (多项式贝叶斯分类器)
**class sklearn.naive_bayes.MultinomialNB(alpha=1.0,fit_prior=True,class_prior=None)**
1. 它假设特征的条件概率分布满足多项式分布
1. 参数：`alpha` `fit_prior` `class_prior`
1. 属性
1. 方法：`fit()` `predict()` `score()` `partial_fit()`
#### 三、BernoulliNB (伯努利贝叶斯分类器)
**class sklearn.naive_bayes.BernoulliNB(alpha=1.0,binarize=0.0,fit_prior=True,class_prior=None)**
1. 它假设特征的条件概率分布满足二项分布
1. 参数：`alpha` `binarize` `fit_prior` `class_prior`
1. 属性
1. 方法：`fit()` `predict()` `score()` `partial_fit()`

#### 注意：`partial_fit()`方法用于递增式学习，可以解决大规模的分类问题
