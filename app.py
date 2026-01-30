from flask import Flask
from flask_cors import CORS
from routes.webhook import webhook_bp
from routes.events import events_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(webhook_bp)
app.register_blueprint(events_bp)

if __name__ == "__main__":
    app.run(debug=True)
