"""Run the app as in the other file."""

from raven import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
