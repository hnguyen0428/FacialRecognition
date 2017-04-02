from flask import Flask
import face_match as fm
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    result = fm.main()
    return jsonify({'match' : result})

if __name__ == "__main__":
    app.run()