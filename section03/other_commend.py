## 其他命令
import redis
conn = redis.Redis()
# 清理集合数据
def clear(key):
	while True:
		if conn.lpop(key) == None:
			break
clear('sort-input')
## sort
conn.rpush('sort-input', 23, 15, 110, 7)
print(conn.sort('sort-input'))
print(conn.sort('sort-input', alpha=True))

## 基于redis的事务
