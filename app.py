from flask import Flask, request, jsonify
import redis
import uuid

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/join_queue', methods=['POST'])
def joinQueue():
    content = request.json
    player_id = str(uuid.uuid4()) # This generates a unique player ID
    skill_level = content['skill_level'] # This is the metric for matchmaking

    # Adding a player to the Redis queue
    redis_client.zadd('matchmaking_queue', {player_id: skill_level})

    return jsonify({'player_id': player_id, 'status': 'queued', 'skill_level': skill_level})

@app.route('/check_status', methods=['GET'])
def check_status():
    player_id = request.args.get('player_id')

    # Mock-up for checking if a player is in a match
    # In a real application, you would check if the player is part of an active match
    # For now, we simulate by checking if the player ID is in a specific Redis set for demonstration
    is_matched = redis_client.sismember('matches', player_id)
    
    status = 'in_game' if is_matched else 'in_queue'

    return jsonify({'player_id': player_id, 'status': status})

if __name__ == '__main__':
    app.run(debug=True)