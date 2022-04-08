from asyncio.windows_events import NULL
from dataclasses import replace
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
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    return render_template("index.html", hostname=hostname, ip=ip)



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
        count = 0
        for line in fstring:
            pattern = re.findall( r'\b(GigabitEthernet0/0/0|GigabitEthernet0/0/1|GigabitEthernet0|VirtualPortGroup0|VirtualPortGroup1)\b', line ) # array
            if pattern:
                temp = line.split()
                for i in pattern:
                    # time.sleep(1)
                    # seed(datetime.now())
                    # r_int = randint(0, 100000)
                    # url = "<a href=\"/" + str(r_int) + "\">"+ str(pattern[0]) +"</a>"
                    # temp[0] = i.replace(str(pattern[0]),url) # replace interface with hyperlink
                    temp.append(str(count))
                    data.append(temp)
                    count = count +1
        data = np.array(data, dtype=list)   
        data =  tuple([tuple(e) for e in data])
        # print(headings)
        # print(data)
    return render_template("interface_table.html", headings=headings, data=data) #, url=url


@app.route('/processes')
def show_proc_mem_sorted():
    with open(r'templates/show_processes_mem_sorted.txt') as msf:
        mstring = msf.readlines()#array of lines
        memline_1 = str(mstring[1])
        mem_headings = memline_1.split()
        mem_headings = np.array(mem_headings)
        mem_headings = np.append(mem_headings, "ID")
        mem_headings = tuple(mem_headings)#makes tuple
        data = []
        for mline in mstring:
            pattern = re.findall(r'\b(Processor Pool Total|reserve P Pool Total|lsmpi_io Pool Total)\b', mline)
            if pattern:
                temp = mline.split()
                for i in pattern:
                    time.sleep(1)
                    seed(datetime.now)
                    r_int = randint(0, 100000)
                    temp.append(str(r_int))
                    data.append(temp)
                    
        data = np.array(data, dtype=list)
        data = tuple([tuple(e) for e in data])
        # print(mem_headings)
        # print(data)
        msf.close()

        return render_template("processes_mem.html", mem_headings=mem_headings, data=data)





@app.route('/interface/<rand_num_str>') # dynamic app route for ip interfaces
def view(rand_num_str):
    selection = NULL
    files = ["templates\show_interface_gigabitethernet000.txt",
    "templates\show_interface_gigabitethernet001.txt",
    "templates\show_interface_virtualportgroup0.txt",
    "templates\show_interface_virtualportgroup0.txt",
    "templates\show_interface_virtualportgroup1.txt"]
    if rand_num_str == "0":
        selection = files[0]
    elif rand_num_str == "1":
        selection = files[1]
    elif rand_num_str == "2":
        selection = files[2]
    elif rand_num_str == "3":
        selection = files[3]
    elif selection == "4":
        selection = files[4]
    else:
        return "Interface Not Found"
    
    with open(selection) as file:
        fstring = file.read()

        pattern = r"(?<=Hardware is )(.+?)(?=, DLY 10 usec,)"
        found = re.findall(pattern, fstring, re.DOTALL)
        joined_string = ' '.join(str(e) for e in found)
        # print(joined_string)

        pattern2 = r"(?<=5 minute)(.+?)(?=0 underruns)"
        found2 = re.findall(pattern2, fstring, re.DOTALL)
        joined_string2 = ' '.join(str(e) for e in found2)
        app_string = "5 minute" + joined_string2 + " 0 underruns"
        replaced_string = app_string.replace("\n", ", ")
        list2  = tuple(map(str, replaced_string.split(', ')))
    return render_template("view_interface.html", p1=joined_string, p2=app_string, list2=list2)


if __name__ == "__main__":
    app.run(host="0.0.0.0") 
    # accessible by any computer 
    # on the network
