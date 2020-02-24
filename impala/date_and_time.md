

### 日期和时间函数
impala支持以下日期和时间函数
- ADD_MONTHS
- ADDDATE
- CURRENT_DATE
- CURRENT_TIMESTAMP
- DATE_ADD
- DATE_PART
- DATE_SUB
- DATE_TRUNC
- DATEDIFF
- DAY
- DAYNAME
- DAYOFWEEK
- DAYOFYEAR
- DAYS_ADD
- DAYS_SUB
- EXTRACT
- FROM_TIMESTAMP
- FROM_UNIXTIME
- FROM_UTC_TIMESTAMP
- HOUR
- HOURS_ADD
- HOURS_SUB
- INT_MONTHS_BETWEEN
- MICROSECONDS_ADD
- MICROSECONDS_SUB
- MILLISECOND
- MILLISECONDS_ADD
- MILLISECONDS_SUB
- MINUTE
- MINUTES_ADD
- MINUTES_SUB
- MONTH
- MONTHNAME
- MONTHS_ADD
- MONTHS_BETWEEN
- MONTHS_SUB
- NANOSECONDS_ADD
- NANOSECONDS_SUB
- NEXT_DAY
- NOW
- QUARTER
- SECOND
- SECONDS_ADD
- SECONDS_SUB
- SUBDATE
- TIMEOFDAY
- TIMESTAMP_CMP
- TO_DATE
- TO_TIMESTAMP
- TO_UTC_TIMESTAMP
- TRUNC
- UNIX_TIMESTAMP
- UTC_TIMESTAMP
- WEEKOFYEAR
- WEEKS_ADD
- WEEKS_SUB
- YEAR
- YEARS_ADD
- YEARS_SUB

下面是对其中一些函数的使用举例：

###### DATE_ADD(TIMESTAMP / DATE date, INT / BIGINT days), DATE_ADD(TIMESTAMP / DATE date, interval_expression)

```sql
select now() as right_now, date_add(now(), interval 3 weeks) as in_3_weeks;
+-------------------------------+-------------------------------+
| right_now                     | in_3_weeks                    |
+-------------------------------+-------------------------------+
| 2016-05-20 11:05:39.173331000 | 2016-06-10 11:05:39.173331000 |
+-------------------------------+-------------------------------+

select now() as right_now, date_add(now(), interval 6 hours) as in_6_hours;
+-------------------------------+-------------------------------+
| right_now                     | in_6_hours                    |
+-------------------------------+-------------------------------+
| 2016-05-20 11:13:51.492536000 | 2016-05-20 17:13:51.492536000 |
+-------------------------------+-------------------------------+

select date_add(cast('2016-01-31' as timestamp), interval 3 months) as 'april_31st';
+---------------------+
| april_31st          |
+---------------------+
| 2016-04-30 00:00:00 |
+---------------------+

```

###### DATE_SUB(TIMESTAMP startdate, INT days), DATE_SUB(TIMESTAMP startdate, interval_expression)


```sql
select now() as right_now, date_sub(now(), 7) as last_week;
+-------------------------------+-------------------------------+
| right_now                     | last_week                     |
+-------------------------------+-------------------------------+
| 2016-05-20 11:21:30.491011000 | 2016-05-13 11:21:30.491011000 |
+-------------------------------+-------------------------------+

select now() as right_now, date_sub(now(), interval 3 weeks) as 3_weeks_ago;
+-------------------------------+-------------------------------+
| right_now                     | 3_weeks_ago                   |
+-------------------------------+-------------------------------+
| 2016-05-20 11:23:05.176953000 | 2016-04-29 11:23:05.176953000 |
+-------------------------------+-------------------------------+

select now() as right_now, date_sub(now(), interval 6 hours) as 6_hours_ago;
+-------------------------------+-------------------------------+
| right_now                     | 6_hours_ago                   |
+-------------------------------+-------------------------------+
| 2016-05-20 11:23:35.439631000 | 2016-05-20 05:23:35.439631000 |
+-------------------------------+-------------------------------+

select date_sub(cast('2016-05-31' as timestamp), interval 1 months) as 'april_31st';
+---------------------+
| april_31st          |
+---------------------+
| 2016-04-30 00:00:00 |
+---------------------+

```

###### TO_TIMESTAMP(BIGINT unixtime), TO_TIMESTAMP(STRING date, STRING pattern)

```sql 
select to_timestamp('Sep 25, 1984', 'MMM dd, yyyy');
+----------------------------------------------+
| to_timestamp('sep 25, 1984', 'mmm dd, yyyy') |
+----------------------------------------------+
| 1984-09-25 00:00:00                          |
+----------------------------------------------+

select to_timestamp('1984/09/25', 'yyyy/MM/dd');
+------------------------------------------+
| to_timestamp('1984/09/25', 'yyyy/mm/dd') |
+------------------------------------------+
| 1984-09-25 00:00:00                      |
+------------------------------------------+

-- One day past the epoch.
select to_timestamp(24 * 60 * 60);
+----------------------------+
| to_timestamp(24 * 60 * 60) |
+----------------------------+
| 1970-01-02 00:00:00        |
+----------------------------+

-- 60 seconds in the past.
select now() as 'current date/time',
  unix_timestamp(now()) 'now in seconds',
  to_timestamp(unix_timestamp(now()) - 60) as '60 seconds ago';
+-------------------------------+----------------+---------------------+
| current date/time             | now in seconds | 60 seconds ago      |
+-------------------------------+----------------+---------------------+
| 2017-10-01 22:03:46.885624000 | 1506895426     | 2017-10-01 22:02:46 |
+-------------------------------+----------------+---------------------+

```

###### TO_UTC_TIMESTAMP(TIMESTAMP ts, STRING timezone)

```sql 
select now() as 'Current time in California USA',
  to_utc_timestamp(now(), 'PDT') as 'Current time in Greenwich UK';
+--------------------------------+-------------------------------+
| current time in california usa | current time in greenwich uk  |
+--------------------------------+-------------------------------+
| 2016-06-01 15:52:08.980072000  | 2016-06-01 22:52:08.980072000 |
+--------------------------------+-------------------------------+

select now() as 'Current time in California USA',
  from_utc_timestamp
  (
    to_utc_timestamp(now(), 'PDT'),
    'EDT'
  ) as 'Current time in New York, USA';
+--------------------------------+-------------------------------+
| current time in california usa | current time in new york, usa |
+--------------------------------+-------------------------------+
| 2016-06-01 18:14:12.743658000  | 2016-06-01 21:14:12.743658000 |
+--------------------------------+-------------------------------+

```

###### UNIX_TIMESTAMP(), UNIX_TIMESTAMP(STRING datetime), UNIX_TIMESTAMP(STRING datetime, STRING format), UNIX_TIMESTAMP(TIMESTAMP datetime)


```sql 
SELECT FROM_UNIXTIME(UNIX_TIMESTAMP(NOW() + interval 3 days),
  'yyyy/MM/dd HH:mm') AS yyyy_mm_dd_hh_mm;
+------------------+
| yyyy_mm_dd_hh_mm |
+------------------+
| 2016/06/03 11:38 |
+------------------+

-- 3 ways of expressing the same date/time in UTC and converting to an integer.

select unix_timestamp('2015-05-15 12:00:00');
+---------------------------------------+
| unix_timestamp('2015-05-15 12:00:00') |
+---------------------------------------+
| 1431691200                            |
+---------------------------------------+

select unix_timestamp('2015-05-15 12:00:00Z');
+----------------------------------------+
| unix_timestamp('2015-05-15 12:00:00z') |
+----------------------------------------+
| 1431691200                             |
+----------------------------------------+

select unix_timestamp
(
  'May 15, 2015 12:00:00',
  'MMM dd, yyyy HH:mm:ss'
) as may_15_month_day_year;
+-----------------------+
| may_15_month_day_year |
+-----------------------+
| 1431691200            |
+-----------------------+

-- 2 ways of expressing the same date and time but in a different timezone.
-- The resulting integer is different from the previous examples.

select unix_timestamp
(
  '2015-05-15 12:00:00-07:00',
  'yyyy-MM-dd HH:mm:ss-hh:mm'
) as may_15_year_month_day;
+-----------------------+
| may_15_year_month_day |
+-----------------------+
| 1431716400            |
+-----------------------+

select unix_timestamp
  (to_utc_timestamp(
    '2015-05-15 12:00:00',
    'PDT')
  ) as may_15_pdt;
+------------+
| may_15_pdt |
+------------+
| 1431716400 |
+------------+

```

###### UTC_TIMESTAMP()

```sql 
select now(), utc_timestamp();
+-------------------------------+-------------------------------+
| now()                         | utc_timestamp()               |
+-------------------------------+-------------------------------+
| 2017-10-01 23:33:58.919688000 | 2017-10-02 06:33:58.919688000 |
+-------------------------------+-------------------------------+

select current_timestamp(), utc_timestamp();
+-------------------------------+-------------------------------+
| current_timestamp()           | utc_timestamp()               |
+-------------------------------+-------------------------------+
| 2017-10-01 23:34:07.400642000 | 2017-10-02 06:34:07.400642000 |
+-------------------------------+-------------------------------+

```


