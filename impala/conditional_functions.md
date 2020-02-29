
## 条件函数
>Apache Impala是一个开源的，原生的Apache Hadoops数据库分析引擎，Apache Impala支持者Cloudera, MapR, Oracle, and Amazon.

>Impala解决Hadoop生态圈无法支持交互式查询的数据分析痛点，早期出现语法完全兼容Hive，现在逐渐支持更多语法，在底层数据库分析join中的优化是有很多创新之处的，特别是针对分布式数据库执行器的优化，利用Bloom Filter让join性能有很大的提升，目前impala建议使用的文件格式是Parquet。

>Impala是一个分布式并行MPP SQL引擎在大数据上的实现，底层调度算法非常灵活，可支持HDFS多副本本地化计算在合并，效率非常高，而且是一个C++实现引擎能高效率使用硬件资源，融入了很多传统关系数据库的设计优势，在分布式查询有很多创新点，融合LLVM优化提升性能，它是一个OLAP引擎。
Impala和HDFS结合做海量数据的交互式分析ad-hoc查询，OLAP场景，BI报表可视化的最佳选择。

Impala支持以下条件函数：

- CASE
- CASE2
- COALESCE
- DECODE
- IF
- IFNULL
- ISFALSE
- ISNOTFALSE
- ISNOTTRUE
- ISNULL
- ISTRUE
- NONNULLVALUE
- NULLIF
- NULLIFZERO
- NULLVALUE
- NVL
- NVL2
- ZEROIFNULL

###### CASE a WHEN b THEN c [WHEN d THEN e]... [ELSE f] END;CASE WHEN a THEN b [WHEN c THEN d]... [ELSE e] END

```sql 
select case x
    when 1 then 'one'
    when 2 then 'two'
    when 0 then 'zero'
    else 'out of range'
  end
    from t1;
---------------------------------------------
select case
    when dayname(now()) in ('Saturday','Sunday') then 'result undefined on weekends'
    when x > y then 'x greater than y'
    when x = y then 'x and y are equal'
    when x is null or y is null then 'one of the columns is null'
    else null
  end
    from t1;
```

###### COALESCE(type v1, type v2, ...)
返回指定的第一个非NULL参数，如果所有参数均为NULL，则返回NULL

###### DECODE(type expression, type search1, type result1 [, type search2, type result2 ...] [, type default] )


```sql 
SELECT event, DECODE(day_of_week, 1, "Monday", 2, "Tuesday", 3, "Wednesday",
  4, "Thursday", 5, "Friday", 6, "Saturday", 7, "Sunday", "Unknown day")
  FROM calendar;
```

