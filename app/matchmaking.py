import redis
import uuid
import time

# Assuming Redis is running on localhost and default port
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def find_matches():
    print("Matchmaking service started...")
    while True:
        # Fetch all players in the queue
        players = redis_client.zrange('matchmaking_queue', 0, -1, withscores=True)
        players.sort(key=lambda x: x[1])  # Sort players by skill level


        time.sleep(5)  # Check for matches every 5 seconds
