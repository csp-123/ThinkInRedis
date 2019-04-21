## 集合
import redis
conn = redis.Redis()

def clear(key):
	while True:
		if conn.spop(key) == None:
			break

clear('set-key')
conn.sadd('set-key', 'a', 'b', 'c')
conn.srem('set-key', 'c', 'd')
print(conn.scard('set-key'))
conn.smove('set-key', 'set-key2', 'a')
print(conn.smembers('set-key'))
print(conn.smembers('set-key2'))

print('-----------------------------')
# SDIFF 返回存在于第一个集合，不存在其他集合的元素
# SDIFFSTORE dest-key key-name 存储版本
# SINTER 返回同时存在于所有集合的元素
# SINTERSTORE dest-key key-name 存储版本
# SUNION 返回至少存在于一个集合中的元素
# SUNIONSTORE dest-key key-name 存储版本
clear('skey1')
clear('skey2')
conn.sadd('skey1', 'a', 'b', 'c', 'd')
conn.sadd('skey2', 'e', 'f', 'c', 'd')

print(conn.sdiff('skey1', 'skey2'))
print(conn.sinter('skey1', 'skey2'))
print(conn.sunion('skey1', 'skey2'))