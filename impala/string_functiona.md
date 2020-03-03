
## 字符串函数
>Apache Impala是一个开源的，原生的Apache Hadoops数据库分析引擎，Apache Impala支持者Cloudera, MapR, Oracle, and Amazon.

>Impala解决Hadoop生态圈无法支持交互式查询的数据分析痛点，早期出现语法完全兼容Hive，现在逐渐支持更多语法，在底层数据库分析join中的优化是有很多创新之处的，特别是针对分布式数据库执行器的优化，利用Bloom Filter让join性能有很大的提升，目前impala建议使用的文件格式是Parquet。

>Impala是一个分布式并行MPP SQL引擎在大数据上的实现，底层调度算法非常灵活，可支持HDFS多副本本地化计算在合并，效率非常高，而且是一个C++实现引擎能高效率使用硬件资源，融入了很多传统关系数据库的设计优势，在分布式查询有很多创新点，融合LLVM优化提升性能，它是一个OLAP引擎。
Impala和HDFS结合做海量数据的交互式分析ad-hoc查询，OLAP场景，BI报表可视化的最佳选择。

Impala支持以下字符串函数：

- ASCII
- BASE64DECODE
- BASE64ENCODE
- BTRIM
- CHAR_LENGTH
- CHR
- CONCAT
- CONCAT_WS
- FIND_IN_SET
- GROUP_CONCAT
- INITCAP
- INSTR
- LEFT
- LENGTH
- LEVENSHTEIN, LE_DST
- LOCATE
- LOWER, LCASE
- LPAD
- LTRI
- PARSE_URL
- REGEXP_ESCAPE
- REGEXP_EXTRACT
- REGEXP_LIKE
- REGEXP_REPLACE
- REPEAT
- REPLACE
- REVERSE
- RIGHT
- RPAD
- RTRIM
- SPACE
- SPLIT_PART
- STRLEFT
- STRRIGHT
- SUBSTR, SUBSTRING
- TRANSLATE
- TRIM
- UPPER, UCASE

###### BASE64DECODE(STRING str)
```sql
-- An arbitrary string can be encoded in base 64.
-- The length of the output is a multiple of 4 bytes,
-- padded with trailing = characters if necessary.
select base64encode('hello world') as encoded,
  length(base64encode('hello world')) as length;
+------------------+--------+
| encoded          | length |
+------------------+--------+
| aGVsbG8gd29ybGQ= | 16     |
+------------------+--------+

-- Passing an encoded value to base64decode() produces
-- the original value.
select base64decode('aGVsbG8gd29ybGQ=') as decoded;
+-------------+
| decoded     |
+-------------+
| hello world |
+-------------+

```

###### BTRIM(STRING a), BTRIM(STRING a, STRING chars_to_trim)
```sql 
-- Remove multiple spaces before and one space after.
select concat('[',btrim('    hello '),']');
+---------------------------------------+
| concat('[', btrim('    hello '), ']') |
+---------------------------------------+
| [hello]                               |
+---------------------------------------+

-- Remove any instances of x or y or z at beginning or end. Leave spaces alone.
select concat('[',btrim('xy    hello zyzzxx','xyz'),']');
+------------------------------------------------------+
| concat('[', btrim('xy    hello zyzzxx', 'xyz'), ']') |
+------------------------------------------------------+
| [    hello ]                                         |
+------------------------------------------------------+

-- Remove any instances of x or y or z at beginning or end.
-- Leave x, y, z alone in the middle of the string.
select concat('[',btrim('xyhelxyzlozyzzxx','xyz'),']');
+----------------------------------------------------+
| concat('[', btrim('xyhelxyzlozyzzxx', 'xyz'), ']') |
+----------------------------------------------------+
| [helxyzlo]                                         |
+----------------------------------------------------+
```

###### CHAR_LENGTH(STRING a), CHARACTER_LENGTH(STRING a)
```sql 
create table length_demo (s string, c char(5));
insert into length_demo values
  ('a',cast('a' as char(5))),
  ('abc',cast('abc' as char(5))),
  ('hello',cast('hello' as char(5)));

select concat('"',s,'"') as s, concat('"',c,'"') as c,
  length(s), length(c),
  char_length(s), char_length(c)
from length_demo;
+---------+---------+-----------+-----------+----------------+----------------+
| s       | c       | length(s) | length(c) | char_length(s) | char_length(c) |
+---------+---------+-----------+-----------+----------------+----------------+
| "a"     | "a    " | 1         | 1         | 1              | 5              |
| "abc"   | "abc  " | 3         | 3         | 3              | 5              |
| "hello" | "hello" | 5         | 5         | 5              | 5              |
+---------+---------+-----------+-----------+----------------+----------------+
```

###### INSTR(STRING str, STRING substr [, BIGINT position [, BIGINT occurrence ] ])
```sql 
select instr('foo bar bletch', 'z');
+------------------------------+
| instr('foo bar bletch', 'z') |
+------------------------------+
| 0                            |
+------------------------------+
select instr('foo bar bletch', 'b', 7);
+---------------------------------+
| instr('foo bar bletch', 'b', 7) |
+---------------------------------+
| 9                               |
+---------------------------------+
select instr('hello world','o',-6);
+-------------------------------+
| instr('hello world', 'o', -6) |
+-------------------------------+
| 5                             |
+-------------------------------+

```

###### LENGTH(STRING a)

```sql 
create table length_demo (s string, c char(5));
insert into length_demo values
  ('a',cast('a' as char(5))),
  ('abc',cast('abc' as char(5))),
  ('hello',cast('hello' as char(5)));

select concat('"',s,'"') as s, concat('"',c,'"') as c,
  length(s), length(c),
  char_length(s), char_length(c)
from length_demo;
+---------+---------+-----------+-----------+----------------+----------------+
| s       | c       | length(s) | length(c) | char_length(s) | char_length(c) |
+---------+---------+-----------+-----------+----------------+----------------+
| "a"     | "a    " | 1         | 1         | 1              | 5              |
| "abc"   | "abc  " | 3         | 3         | 3              | 5              |
| "hello" | "hello" | 5         | 5         | 5              | 5              |
+---------+---------+-----------+-----------+----------------+----------------+
```

###### REGEXP_ESCAPE(STRING source)
```sql 
+------------------------------------------------------+
| regexp_escape('Hello.world')                         |
+------------------------------------------------------+
| Hello\.world                                         |
+------------------------------------------------------+
```

###### REGEXP_EXTRACT(STRING subject, STRING pattern, INT index)
```sql 
select regexp_extract('abcdef123ghi456jkl','.*?(\\d+)',0);
+------------------------------------------------------+
| regexp_extract('abcdef123ghi456jkl', '.*?(\\d+)', 0) |
+------------------------------------------------------+
| abcdef123ghi456                                      |
+------------------------------------------------------+
select regexp_extract('abcdef123ghi456jkl','.*?(\\d+)',1);
+------------------------------------------------------+
| regexp_extract('abcdef123ghi456jkl', '.*?(\\d+)', 1) |
+------------------------------------------------------+
| 456                                                  |
+------------------------------------------------------+
select regexp_extract('AbcdBCdefGHI','.*?([[:lower:]]+)',1);
+--------------------------------------------------------+
| regexp_extract('abcdbcdefghi', '.*?([[:lower:]]+)', 1) |
+--------------------------------------------------------+
| def                                                    |
+--------------------------------------------------------+
select regexp_extract('AbcdBCdefGHI','.*?([[:lower:]]+).*?',1);
+-----------------------------------------------------------+
| regexp_extract('abcdbcdefghi', '.*?([[:lower:]]+).*?', 1) |
+-----------------------------------------------------------+
| bcd                                                       |
+-----------------------------------------------------------+
```

###### REGEXP_LIKE(STRING source, STRING pattern[, STRING options])
```sql 
select regexp_like('foo','f');
+-------------------------+
| regexp_like('foo', 'f') |
+-------------------------+
| true                    |
+-------------------------+
+---------------------------------------+
| regexp_like('foooooobar', 'fx*y*o*b') |
+---------------------------------------+
| true                                  |
+---------------------------------------+
```

###### REGEXP_REPLACE(STRING initial, STRING pattern, STRING replacement)
```sql 
select regexp_replace('aaabbbaaa','b+','xyz');
+------------------------------------------+
| regexp_replace('aaabbbaaa', 'b+', 'xyz') |
+------------------------------------------+
| aaaxyzaaa                                |
+------------------------------------------+
select regexp_replace('123-456-789','[^[:digit:]]','');
+---------------------------------------------------+
| regexp_replace('123-456-789', '[^[:digit:]]', '') |
+---------------------------------------------------+
| 123456789                                         |
+---------------------------------------------------+
```


###### REPLACE(STRING initial, STRING target, STRING replacement)
```sql 
select replace('hello world','world','earth');
+------------------------------------------+
| replace('hello world', 'world', 'earth') |
+------------------------------------------+
| hello earth                              |
+------------------------------------------+
```


###### SPLIT_PART(STRING source, STRING delimiter, BIGINT index)
```sql 
SPLIT_PART('x,y,z',',',2) returns 'y'.

SPLIT_PART('one***two***three','***',2) returns 'two'.

SPLIT_PART('abc@@def@@ghi', '@@', 3) returns 'ghi'.

SPLIT_PART('abc@@def@@ghi', '@@', -3) returns 'abc'.
```

###### TRANSLATE(STRING input, STRING from, STRING to)
```sql 
translate('abcdedg', 'bcd', '1') returns 'a1eg'.

translate('Unit Number#2', '# ', '_') returns 'UnitNumber_2'.
```