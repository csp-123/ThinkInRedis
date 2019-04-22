## 有序集合
import redis
conn = redis.Redis()
conn.zadd('zset-key', {'a': 3, 'b': 2, 'c': 1})
print(conn.zcard('zset-key'))
conn.zincrby('zset-key', 3, 'c')
print(conn.zscore('zset-key', 'b'))
print(conn.zrank('zset-key', 'c'))
print(conn.zcount('zset-key', 0, 3))
conn.zrem('zset-key', 'b')
print(conn.zrange('zset-key', 0, -1, withscores=True))

print('---------------------------------------')

