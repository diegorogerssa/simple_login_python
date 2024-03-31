from flask import Flask
from controllers.user import user

app = Flask(__name__)
app.register_blueprint(user)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)