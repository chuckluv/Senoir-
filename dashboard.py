from flask import Flask, render_template, url_for
import socket
from subprocess import check_output
import re
import numpy as np
import time
from datetime import datetime
from random import seed, randint
from cpu_statistics import cpu_stats_json, cpu_percent_json, cpu_freq_json, show_processes_cpu_sorted

app = Flask(__name__)

@app.route("/")
def api_root():
    return "Connection Successful"

@app.route("/home")
def home():
    show_ip()
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


@app.route('/background_process_timed_cpu')
def refresh():
    cpu_stats_json()
    cpu_percent_json()
    cpu_freq_json()
    show_processes_cpu_sorted()
    return("nothing")


@app.route('/background_cpu_table')
def refreshCPUtable():
    return render_template("table.html")



@app.route('/interface')
# def test():
#     return render_template("ip_interface.html")

def show_ip():
    # Prints interfaces to console
    path = r"\templates\ip_interface.html"

    with open(r'templates\show_ip_interface_brief.txt') as fh:
        fstring = fh.readlines() # array of lines
        line_1 = str(fstring[1])
        headings = line_1.split()
        headings = np.array(headings)
        headings = np.append(headings, "ID")
        headings =  tuple(headings) # turns array into tuple
        data = []
        for line in fstring:
            pattern = re.findall( r'\b(GigabitEthernet0/0/0|GigabitEthernet0/0/1|GigabitEthernet0|VirtualPortGroup0|VirtualPortGroup1)\b', line ) # array
            if pattern:
                temp = line.split()
                for i in pattern:
                    time.sleep(1)
                    seed(datetime.now())
                    r_int = randint(0, 100000)
                    # url = "<a href=\"/" + str(r_int) + "\">"+ str(pattern[0]) +"</a>"
                    # temp[0] = i.replace(str(pattern[0]),url) # replace interface with hyperlink
                    temp.append(str(r_int))
                    data.append(temp)
        data = np.array(data, dtype=list)   
        data =  tuple([tuple(e) for e in data])
        print(headings)
        print(data)
        fh.close()
    return render_template("interface_table.html", headings=headings, data=data) #, url=url



    # with open('templates\ip_interface.html', 'w') as file:
    #     file.write("<p>")
    #     file.write(fstring[1])
    #     file.close()

    # for line in fstring:
        # pattern = re.findall( r'\b(GigabitEthernet0/0/0|GigabitEthernet0/0/1|GigabitEthernet0|VirtualPortGroup0|VirtualPortGroup1)\b', line ) # array
        # ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line ) # array
        # if pattern:
    #         fd=open("templates\ip_interface.html","a")
    #         fd.write(line)
    #         fd.write("<br>")
    #         fd.close()
            # if pattern:
            #     for i in pattern:
            #         seed(datetime.now())
            #         r_int = randint(0, 100000)
            #         with open(r'templates\ip_interface.html') as file:
            #             filedata = file.read() # array of lines
            #             url = "<a href=\"interface/" + str(r_int) + "\">"+ str(pattern[0]) +"</a>"
            #             filedata = filedata.replace(str(pattern[0]),url) # replace interface with hyperlink
            #         with open('templates\ip_interface.html', 'w') as file:
            #             file.write(filedata)
    # with open('templates\ip_interface.html', 'a') as file:
    #     file.write("</p>") 
    #     file.close()
    # fh.close()  # close demo.txt

@app.route('/interface/<rand_num_str>') # dynamic app route for ip interfaces
def view(rand_num_str):
    if type(rand_num_str) == str:
        return "Viewing Interface"
    else:
        return "404 Not Found"


if __name__ == "__main__":
    app.run(host="0.0.0.0") 
    # accessible by any computer 
    # on the network
