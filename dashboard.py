from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def api_root():
    return "Connection Successful"

@app.route("/home")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0") 
    # accessible by any computer 
    # on the network
