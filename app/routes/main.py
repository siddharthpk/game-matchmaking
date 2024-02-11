from flask import Blueprint, request, jsonify
import uuid
import redis

main_blueprint = Blueprint('main', __name__)

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@main_blueprint.route('/join_queue', methods=['POST'])
def joinQueue():
    content = request.json
    player_id = str(uuid.uuid4()) # This generates a unique player ID
    skill_level = content['skill_level'] # This is the metric for matchmaking

    # Check if the skill level is provided
    if skill_level is None:
        return jsonify({"error": "Skill level is required"}), 400
    
    # Adding a player to the Redis queue
    redis_client.zadd('matchmaking_queue', {player_id: skill_level})

    return jsonify({'player_id': player_id, 'status': 'queued', 'skill_level': skill_level}), 200

@main_blueprint.route('/check_status', methods=['GET'])
def check_status():
    player_id = request.args.get('player_id')

    if not player_id:
        return jsonify({"error": "Player ID is required"}), 400

    # Check if the player is in the matchmaking queue
    in_queue = redis_client.zscore('matchmaking_queue', player_id) is not None

    # Assuming we move matched players to an 'in_game' set
    in_game = redis_client.sismember('in_game', player_id)

    if in_game:
        status = 'in_game'
    elif in_queue:
        status = 'in_queue'
    else:
        status = 'unknown'  # Player not found in queue or in a game

    return jsonify({"player_id": player_id, "status": status}), 200
