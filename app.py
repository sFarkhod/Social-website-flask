from website import createapp

if __name__ == '__main__':
    socketio, app = createapp()
    socketio.run(app, debug=True, port=5000)


