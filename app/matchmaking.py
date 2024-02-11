import redis
import uuid
import time

# Assuming Redis is running on localhost and default port
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def find_matches():
    print("Matchmaking service started...")
    while True:
        all_players = redis_client.zrangebyscore('matchmaking_queue', '-inf', '+inf', withscores=True)
        matched_players = []

        for i in range(len(all_players) - 1):
            player1 = all_players[i]
            player2 = all_players[i + 1]

            # Check if players' skill levels are within a threshold, e.g., 10
            if abs(player1[1] - player2[1]) <= 10 and player1[0] not in matched_players and player2[0] not in matched_players:
                # Generate a unique match ID
                match_id = str(uuid.uuid4())

                 # For each matched player, store the match ID they're part of
                redis_client.hset('player_matches', player1[0], match_id)
                redis_client.hset('player_matches', player2[0], match_id)

                # Remove players from the matchmaking queue
                redis_client.zrem('matchmaking_queue', player1[0], player2[0])

                # Keep track of matched players to avoid rematching in the same loop
                matched_players.extend([player1[0], player2[0]])

                print(f"Matched {player1[0]} and {player2[0]} in match {match_id}")
        time.sleep(5)  # Check for matches every 5 seconds
