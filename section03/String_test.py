## 字符串
# 字符串可以存储以下三种类型的值
# 字节串、整数、浮点数
import redis
conn = redis.Redis()
print(conn.get('key'))
print(conn.incr('key'))
print(conn.incr('key', 15))
conn.decr('key', 5)
print(conn.get('key'))
conn.set('key', '13')
print(conn.incr('key'))

print('-------------------')
conn.set('new-string-key', '')
conn.append('new-string-key', 'hello ')
conn.append('new-string-key', 'world!')
print(conn.get('new-string-key'))

print(conn.getrange('new-string-key', 3, 7))
conn.setrange('new-string-key', 0, 'H')
conn.setrange('new-string-key', 6, 'W')
print(conn.get('new-string-key'))

conn.setrange('new-string-key', 11, ', how are you?')
print(conn.get('new-string-key'))

print(conn.setbit('another-key', 2, 1))
print(conn.setbit('another-key', 7, 1))
print(conn.get('another-key'))