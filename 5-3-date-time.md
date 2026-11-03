---
title: '5.3 Date and Time (optional)'
---

::::::::::::::::::::::::::::::::::::: callout

## Optional section

This section is optional. It belongs with Week 5, but nothing in the course depends on it.

::::::::::::::::::::::::::::::::::::::::::::::::

## Python *datetime*

Python has got _datetime_ module to handle date and time.

```python
import datetime  # modules are explained in Week 6 - leave the import lines in this section as they are
print(dir(datetime))
```

```output
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
```

With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on _date_, _datetime_, _time_ and _timedelta_. Let us see them one by one.

### Getting *datetime* Information

```python
from datetime import datetime
now = datetime.now()             # the comments show 2 November 2026 at 14:05 - yours will show the date and time you run it
print(now)                      # 2026-11-02 14:05:09.549883
day = now.day                   # 2
month = now.month               # 11
year = now.year                 # 2026
hour = now.hour                 # 14
minute = now.minute             # 5
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)   # 2 11 2026 14 5
print('timestamp', timestamp)           # timestamp 1793599509.549883 (depends on your time zone)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 2/11/2026, 14:5
```

Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

### Formatting Date Output Using *strftime*

```python
from datetime import datetime
new_year = datetime(2027, 1, 1)
print(new_year)      # 2027-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 1 1 2027 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2027, 0:0

```

Formatting date time using *strftime* method and the documentation can be found [strftime.org](https://strftime.org/).

```python
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 14:05:09
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YYYY H:M:S format (used in the USA)
print("time one:", time_one)        # time one: 11/02/2026, 14:05:09
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YYYY H:M:S format (used in Australia)
print("time two:", time_two)        # time two: 02/11/2026, 14:05:09
```

Your output will show the date and time you run it, for example:

```output
time: 14:05:09
time one: 11/02/2026, 14:05:09
time two: 02/11/2026, 14:05:09
```

Here are all the _strftime_ symbols we use to format time. An example of all the formats for this module.

| Directive | Description | Example |
|---|---|---|
| `%a` | Weekday, short version | Wed |
| `%A` | Weekday, full version | Wednesday |
| `%w` | Weekday as a number 0-6, 0 is Sunday | 3 |
| `%d` | Day of month 01-31 | 31 |
| `%b` | Month name, short version | Dec |
| `%B` | Month name, full version | December |
| `%m` | Month as a number 01-12 | 12 |
| `%y` | Year, short version, without century | 18 |
| `%Y` | Year, full version | 2018 |
| `%H` | Hour 00-23 | 17 |
| `%I` | Hour 00-12 | 05 |
| `%p` | AM/PM | PM |
| `%M` | Minute 00-59 | 41 |
| `%S` | Second 00-59 | 08 |
| `%f` | Microsecond 000000-999999 | 548513 |
| `%z` | UTC offset | +0100 |
| `%Z` | Timezone | CST |
| `%j` | Day number of year 001-366 | 365 |
| `%U` | Week number of year, Sunday as the first day of week, 00-53 | 52 |
| `%W` | Week number of year, Monday as the first day of week, 00-53 | 52 |
| `%c` | Local version of date and time | Mon Dec 31 17:41:00 2018 |
| `%x` | Local version of date | 12/31/18 |
| `%X` | Local version of time | 17:41:00 |
| `%%` | A % character | % |

### String to Time Using *strptime*
Here is [documentation](https://www.programiz.com/python-programming/datetime/strptime) that helps to understand the format. 

```python
from datetime import datetime
date_string = "2 November, 2026"
print("date_string =", date_string)     # date_string = 2 November, 2026
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2026-11-02 00:00:00
```

### Using *date* from *datetime*

```python
from datetime import date
d = date(2027, 1, 1)
print(d)        # 2027-01-01
print('Current date:', date.today())  # e.g. 2026-11-02 - the day you run it
# date object of today's date
today = date.today()
print("Current year:", today.year)   # e.g. 2026
print("Current month:", today.month) # e.g. 11
print("Current day:", today.day)     # e.g. 2
```

### Time Objects to Represent Time

```python
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555
```

```output
a = 00:00:00
b = 10:30:50
c = 10:30:50
d = 10:30:50.200555
```

### Difference Between Two Points in Time Using *date* and *datetime*

```python
from datetime import date, datetime
today = date(year=2026, month=11, day=2)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  60 days, 0:00:00

t1 = datetime(year = 2026, month = 11, day = 2, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 59 days, 23:01:00
```

### Difference Between Two Points in Time Using *timedelta*

```python
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)   # t3 = 86 days, 22:56:50
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

1. Get the current day, month, year, hour, minute and timestamp from datetime module
2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
3. The date string is "2 November, 2026". Change this string to a datetime object.
4. Calculate the time difference between now and new year.
5. Calculate the time difference between 1 January 1970 and now.
6. Think, what can you use the datetime module for? Examples:
   - Time series analysis
   - To get a timestamp of any activities in an application
   - Adding posts on a blog

::::::::::::::::::::::::::::::::::::::::::::::::

