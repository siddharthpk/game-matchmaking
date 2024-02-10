from app import create_app
from threading import Thread
from app.matchmaking import find_matches

app = create_app()

if __name__ == '__main__':
    # Run the matchmaking logic in a separate thread
    matchmaking_thread = Thread(target=find_matches)
    matchmaking_thread.daemon = True
    matchmaking_thread.start()

    app.run(debug=True)
