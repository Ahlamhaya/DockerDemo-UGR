from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>This is a docker demo made for the purpose of defending my thesis under the title : Use of containers to deploy AI applications</h1>"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080) 