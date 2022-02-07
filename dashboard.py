from flask import Flask, render_template, url_for
import socket
from subprocess import check_output
import psutil # before running pip install psutil

app = Flask(__name__)

@app.route("/")
def api_root():
    return "Connection Successful"

@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/background_process_test')
def background_process_test():
    print(socket.gethostname())
    return ("nothing")

@app.route('/background_process_ip')
def background_process_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0]) # gets IP
    return ("nothing")

@app.route('/background_process_cpu')
def background_process_cpu():
    print("CPU Percent\n" + str(psutil.cpu_percent()))
    print("CPU Stats\n" + str(psutil.cpu_stats()))
    print("CPU Frequency\n"  + str(psutil.cpu_freq()))
    return("nothing")


if __name__ == "__main__":
    app.run(host="0.0.0.0") 
    # accessible by any computer 
    # on the network
