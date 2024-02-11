# Game Matchmaking System

This project implements a basic game matchmaking system using Flask and Redis. It allows players to join a matchmaking queue and pairs them based on skill levels. The system supports checking a player's status to determine if they have been matched.

## Features

- Add players to a matchmaking queue with a skill level.
- Automatically match players based on skill levels.
- Check the matchmaking status of a player.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- Redis
- Docker (optional, for running Redis in a container)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/siddharthpk/game-matchmaking.git
   cd game-matchmaking
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start Redis**

   - **Using Docker:**

     ```bash
     docker run --name redis-matchmaking -p 6379:6379 -d redis
     ```

   - **Locally:**

     Ensure Redis is installed and start it according to your system's instructions.

### Running the Application

1. **Start the Flask application**

   ```bash
   python app.py
   ```

   This command starts the Flask server and the matchmaking process.

## Testing the Application

Use `curl` commands to test adding players to the matchmaking queue and checking their status.

### Add Players to the Queue

```bash
# Replace <skill_level> with the desired float type skill level of the player
curl -X POST http://localhost:5000/join_queue -H "Content-Type: application/json" -d '{"skill_level": <skill_level>}'
```

Example:

```bash
curl -X POST http://localhost:5000/join_queue -H "Content-Type: application/json" -d '{"skill_level": 10.5}'
```

### Check Player Status

```bash
# Replace <player_id> with the actual player ID returned by the /join_queue request
curl "http://localhost:5000/check_status?player_id=<player_id>"
```

## Development and Contributions

Feel free to fork the repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

Ensure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
