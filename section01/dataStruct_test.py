## 1.2.1 redis中的字符串 string
## SET GET DEL使用实例
# redis-cli
# set hello world
# get hello
# del hello

## 1.2.2 redis中的列表 list
# lpush lpop lindex
# lrange list-key 0 -1 查看列表

## 1.2.3 redis中的集合 set
# sadd set-key item
# smembers set-key
# sismember set-key item3
# srem set-key item3

## 1.2.4 redis中的散列
# hset hash-key sub-key1 value1
# hgetall hash-key
# hdel hash-key sub-key2
# hget hash-key sub-key1

## 1.2.5 redis中的有序集合
# zadd zset-key 728 member1
# zrange zset-key 0 -1 withscores
# zrangebyscore zset-key 0 800 withscores
# zrem zset-key member1
