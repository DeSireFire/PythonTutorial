from datetime import datetime,timedelta

"""
timedelta代表两个datetime之间的时间差
"""
now = datetime(2011,11,12,13,14,16,16)
past = datetime(2010,11,12,13,14,15,16)

timespan = now - past
print(timespan)
print(timespan.days)
print(timespan.total_seconds())
print(type(timespan))
print(dir(timespan))

t1 = timedelta(days=1)
t2 = now +t1
print(type(t2))
print(t2)

