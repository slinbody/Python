# It will show any error message
try:
    open('/tmp/123','r')
except Exception as ex:
    print type(ex).__name__
    print ex
