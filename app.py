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

if __name__ == '__main__':
    app.run(debug=True)