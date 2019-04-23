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
# 无事务运行
import threading, time
def notrans():
	print(conn.incr('notrans:'))
	time.sleep(1)
	conn.incr('notrans:', -1)

if 1:
	for i in range(3):
		threading.Thread(target=notrans).start()
	time.sleep(.5)


def trans():
	pipeline = conn.pipeline()
	pipeline.incr('trans:')
	time.sleep(1)
	pipeline.incr('trans:', -1)
	print(pipeline.execute()[0])

if 1:
	for i in range(3):
		threading.Thread(target=trans).start()
	time.sleep(.5)

## 键的过期时间
conn.set('key', 'value')
print(conn.get('key'))
conn.expire('key', 2)
time.sleep(2)
print(conn.get('key'))
conn.set('key', 'value2')

conn.expire('key', 100)
print(conn.ttl('key'))