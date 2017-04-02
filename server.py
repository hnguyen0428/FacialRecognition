from flask import Flask
from flask_cors import CORS
import face_match as fm
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    result = fm.main()
    return jsonify({'match' : result})

if __name__ == "__main__":
    app.run()