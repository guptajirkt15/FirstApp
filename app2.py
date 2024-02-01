from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is second app! </h1>"

if __name__ == '__main__':
    app.run(debug=True , port=5001)
