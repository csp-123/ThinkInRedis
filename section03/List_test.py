## 列表
import redis
conn = redis.Redis()
# 清理集合数据
def clear(key):
	while True:
		if conn.lpop(key) == None:
			break
clear('list-key')
print(conn.rpush('list-key', 'last'))
print(conn.lpush('list-key', 'first'))
print(conn.rpush('list-key', 'new last'))
print(conn.lrange('list-key', 0, -1))
print(conn.rpush('list-key', 'a', 'b', 'c'))
print(conn.lrange('list-key', 0, -1))
print(conn.ltrim('list-key', 2, -1))
print(conn.lrange('list-key', 0, -1))
print('-----------------------------')

# BLPOP BRPOP key-name timeout(s) 阻塞式命令
# RPOPLPUSH BRPOPLPUSH(timeout阻塞式) 
clear('list')
clear('list2')
conn.lpush('list', 'item')
conn.lpush('list', 'item1')
conn.lpush('list2', 'item2')
conn.brpoplpush('list2', 'list', 1)
print(conn.lrange('list', 0, -1))
print(conn.lrange('list2', 0, -1))

