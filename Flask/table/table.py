#!flask/bin/python
from app import app, db, serve
from app.models import Tickers


@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'Tickers':Tickers}

if __name__ == "__main__":
    # app.run(debug = True)
    app.debug = True
    serve(app, host = '127.0.0.1', port = 5000)