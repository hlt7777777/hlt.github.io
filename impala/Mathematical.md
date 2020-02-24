
## 数学函数
- ABS
- ACOS
- ASIN
- ATAN
- ATAN2
- BIN
- CEIL, CEILING, DCEIL
- CONV
- COS
- COSH
- COT
- DEGREES
- E
- EXP
- FACTORIAL
- FLOOR, DFLOOR
- FMOD
- FNV_HASH
- GREATEST
- HEX
- IS_INF
- IS_NAN
- LEAST
- LN
- LOG
- LOG10
- LOG2
- MAX_INT, MAX_TINYINT, MAX_SMALLINT, MAX_BIGINT
- MIN_INT, MIN_TINYINT, MIN_SMALLINT, MIN_BIGINT
- MOD
- MURMUR_HASH
- NEGATIVE
- PI
- PMOD
- POSITIVE
- POW, POWER, DPOW, FPOW
- PRECISION
- QUOTIENT
- RADIANS
- RAND, RANDOM
- ROUND, DROUND
- SCALE
- SIGN
- SIN
- SINH
- SQRT
- TAN
- TANH
- TRUNCATE, DTRUNC, TRUNC
- UNHEX
- WIDTH_BUCKET

下面是一些举例：
###### FACTORIAL(integer_type a)

```sql
select factorial(5);
+--------------+
| factorial(5) |
+--------------+
| 120          |
+--------------+

select 5!;
+-----+
| 5!  |
+-----+
| 120 |
+-----+

```
###### FMOD(DOUBLE a, DOUBLE b), FMOD(FLOAT a, FLOAT b)

```sql
select fmod(10,3);
+-------------+
| fmod(10, 3) |
+-------------+
| 1           |
+-------------+

select fmod(5.5,2);
+--------------+
| fmod(5.5, 2) |
+--------------+
| 1.5          |
+--------------+

select 10 % 3;
+--------+
| 10 % 3 |
+--------+
| 1      |
+--------+

select 5.5 % 2;
+---------+
| 5.5 % 2 |
+---------+
| 1.5     |
+---------+

```

###### MOD(numeric_type a, same_type b)


```sql
select mod(10,3);
+-------------+
| mod(10, 3) |
+-------------+
| 1           |
+-------------+

select mod(5.5,2);
+--------------+
| mod(5.5, 2) |
+--------------+
| 1.5          |
+--------------+

``` 

