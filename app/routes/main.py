from flask import Blueprint, request, jsonify
import uuid
import redis

main_blueprint = Blueprint('main', __name__)

#  Redis is running on localhost and default port
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@main_blueprint.route('/join_queue', methods=['POST'])
def joinQueue():
    content = request.json
    player_id = str(uuid.uuid4()) # This generates a unique player ID
    skill_level = content['skill_level'] # This is the metric for matchmaking

    # Check if the skill level is provided
    if skill_level is None:
        try:
            skill_level = float(skill_level)  # Ensure skill level is a valid float
        except ValueError:
            return jsonify({"error": "Skill level is required"}), 400
    
    # Adding a player to the Redis queue
    redis_client.zadd('matchmaking_queue', {player_id: skill_level})

    return jsonify({'player_id': player_id, 'status': 'queued', 'skill_level': skill_level}), 200

@main_blueprint.route('/check_status', methods=['GET'])
def check_status():
    player_id = request.args.get('player_id')

    if not player_id:
        return jsonify({"error": "Player ID is required"}), 400

   # # Check if the player is associated with a match ID in the 'player_matches' hash
    match_id = redis_client.hget('player_matches', player_id)
    if match_id:
        status = 'in_game'
    else:
        # Additionally, check if they're still in the matchmaking queue
        in_queue = redis_client.zscore('matchmaking_queue', player_id) is not None
        status = 'in_queue' if in_queue else 'unknown'


    return jsonify({"player_id": player_id, "status": status}), 200
