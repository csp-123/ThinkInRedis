## 散列
import redis
conn = redis.Redis()
conn.hmset('hash-key', {'k1':'v1', 'k2':'v2', 'k3':'v3'})
print(conn.hmget('hash-key', ['k2', 'k3']))
print(conn.hgetall('hash-key'))
print(conn.hlen('hash-key'))
conn.hdel('hash-key', 'sub-key1')
print(conn.hgetall('hash-key'))
print(conn.hlen('hash-key'))

print('------------------')
conn.hmset('hash-key2', {'short':'hello', 'long':1000 * '1'})
print(conn.hkeys('hash-key2'))
print(conn.hvals('hash-key2'))
print(conn.hexists('hash-key2', 'num'))
print(conn.hincrby('hash-key2', 'num'))
print(conn.hexists('hash-key2', 'num'))
print(conn.hmget('hash-key2', 'num'))