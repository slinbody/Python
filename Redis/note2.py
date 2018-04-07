# the set of python in redis
# ref https://blog.csdn.net/u012894975/article/details/51326091
import redis_lib
import redis

redis_db = redis.StrictRedis(host=redis_lib.redis_server, port=6379, db=0)

redis_db.sadd('0407','12')          # add element to set
redis_db.sadd('0407','123')
redis_db.sadd('0407','123','55')
redis_db.smembers('0407')           # show element in set
redis_db.srem('0407','123')         # remove element in set
