import redis

def connect_to_redis():
    r = redis.Redis(host="localhost", port=6379, db=0)
    return r
