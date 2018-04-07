# about dict of dict in redis
import redis

redis_db = redis.StrictRedis(host='xxx.aaa.com', port=6379, db=0)
user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}

redis_db.hmset("TEST1", user) 

redis_db.hgetall("TEST1")
# {'Company': 'SCTL', 'Address': 'Mumbai', 'Location': 'RCP', 'Name': 'Pradeep'}

redis_db.hset("TEST1", "Name", "Pradeep11")

redis_db.hgetall("TEST1")
# {'Company': 'SCTL', 'Address': 'Mumbai', 'Location': 'RCP', 'Name': 'Pradeep111'}

redis_db.keys()
redis_db.delete("TEST1")

