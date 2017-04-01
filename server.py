from flask import Flask
import face_match as fm

app = Flask(__name__)

@app.route('/')
def index():
    result = fm.main()
    return result

if __name__ == "__main__":
    app.run()