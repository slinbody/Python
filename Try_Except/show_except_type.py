try:
    open('/tmp/123','r')
except Exception as ex:
    print type(ex).__name__
