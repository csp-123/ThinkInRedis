## 有序集合
import redis
conn = redis.Redis()
conn.zadd('zset-key', 'a', 3)
print(conn.zcard('zset-key'))
print(conn.zrange('zset-key', 0, -1, withscores=True))