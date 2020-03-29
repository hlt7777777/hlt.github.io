


## mysql日期与时间函数

- ADDDATE()
- ADDTIME()
- CONVERT_TZ()
- CURDATE()
- CURRENT_DATE(), CURRENT_DATE
- CURRENT_TIME(), CURRENT_TIME
- CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP
- CURTIME()
- DATE()
- DATE_ADD()
- DATE_FORMAT()
- DATE_SUB()
- DATEDIFF()
- DAY()
- DAYNAME()
- DAYOFMONTH()
- DAYOFWEEK()
- DAYOFYEAR()
- EXTRACT()
- FROM_DAYS()
- FROM_UNIXTIME()
- GET_FORMAT()
- HOUR()
- LAST_DAY
- LOCALTIME(), LOCALTIME
- LOCALTIMESTAMP, LOCALTIMESTAMP()
- MAKEDATE()
- MAKETIME()
- MICROSECOND()
- MINUTE()
- MONTH()
- MONTHNAME()
- NOW()
- PERIOD_ADD()
- PERIOD_DIFF()
- QUARTER()
- SEC_TO_TIME()
- SECOND()
- STR_TO_DATE()
- SUBDATE()
- SUBTIME()
- SYSDATE()
- TIME()
- TIME_FORMAT()
- TIME_TO_SEC()
- TIMEDIFF()
- TIMESTAMP()
- TIMESTAMPADD()
- TIMESTAMPDIFF()
- TO_DAYS()
- TO_SECONDS()
- UNIX_TIMESTAMP()
- UTC_DATE()
- UTC_TIME()
- UTC_TIMESTAMP()
- WEEK()
- WEEKDAY()
- WEEKOFYEAR()
- YEAR()
- YEARWEEK()


ADDDATE(date,INTERVAL expr unit), ADDDATE(expr,days)
```sql
mysql> SELECT DATE_ADD('2008-01-02', INTERVAL 31 DAY);
        -> '2008-02-02'
mysql> SELECT ADDDATE('2008-01-02', INTERVAL 31 DAY);
        -> '2008-02-02'
```
CONVERT_TZ(dt,from_tz,to_tz)
```sql
mysql> SELECT CONVERT_TZ('2004-01-01 12:00:00','GMT','MET');
        -> '2004-01-01 13:00:00'
mysql> SELECT CONVERT_TZ('2004-01-01 12:00:00','+00:00','+10:00');
        -> '2004-01-01 22:00:00'
```
CURDATE()
```sql
mysql> SELECT CURDATE();
        -> '2008-06-13'
mysql> SELECT CURDATE() + 0;
        -> 20080613
```

```sql
mysql> SELECT CURTIME();
        -> '23:50:26'
mysql> SELECT CURTIME() + 0;
        -> 235026.000000
```
DATE_FORMAT(date,format)
```sql
mysql> SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
        -> 'Sunday October 2009'
mysql> SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');
        -> '22:23:00'
mysql> SELECT DATE_FORMAT('1900-10-04 22:23:00',
    ->                 '%D %y %a %d %m %b %j');
        -> '4th 00 Thu 04 10 Oct 277'
mysql> SELECT DATE_FORMAT('1997-10-04 22:23:00',
    ->                 '%H %k %I %r %T %S %w');
        -> '22 22 10 10:23:00 PM 22:23:00 00 6'
mysql> SELECT DATE_FORMAT('1999-01-01', '%X %V');
        -> '1998 52'
mysql> SELECT DATE_FORMAT('2006-06-00', '%d');
        -> '00'
```


```sql
mysql> SELECT FROM_UNIXTIME(1447430881);
        -> '2015-11-13 10:08:01'
mysql> SELECT FROM_UNIXTIME(1447430881) + 0;
        -> 20151113100801
mysql> SELECT FROM_UNIXTIME(1447430881,
    ->                      '%Y %D %M %h:%i:%s %x');
        -> '2015 13th November 10:08:01 2015'
```


