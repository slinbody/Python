def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
        
        
>>> import datetime
>>> start = datetime.time(23, 0, 0)
>>> end = datetime.time(1, 0, 0)
>>> time_in_range(start, end, datetime.time(23, 30, 0))
True
>>> time_in_range(start, end, datetime.time(12, 30, 0))
False

========= To be continue ==============
