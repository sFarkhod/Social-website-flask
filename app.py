from website import createapp

if __name__ == '__main__':
    app = createapp()
    app.run(debug=True, port=5000)


