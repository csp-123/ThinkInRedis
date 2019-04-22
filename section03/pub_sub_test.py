## 发布与订阅
import redis
import time
import threading
conn = redis.Redis()
def publisher(n):
	time.sleep(1)
	for i in range(n):
		# 发布一条消息
		conn.publish('channel', i)
		time.sleep(1)

def run_pubsub():
	# 启动发送者线程，并发送三条消息
	threading.Thread(target=publisher, args=(3,)).start()
	# 创建发布与订阅对象， 并订阅给定的频道
	pubsub = conn.pubsub()
	pubsub.subscribe(['channel'])
	count = 0
	for item in pubsub.listen():
		print(item)
		count += 1
		if count == 4:
			# 在接收到一条订阅反馈消息和三条发布者发送的消息后执行退订操作
			pubsub.unsubscribe()
		if count == 5:
			# 客户端在接收到退订反馈消息后就退出循环
			break

run_pubsub()