import json
from sre_parse import State
from textwrap import indent
from flask import Flask, render_template, url_for
from subprocess import check_output
import psutil # before running pip install psutil
import time

# print("CPU Percent\n" + str(psutil.cpu_percent()))
def cpu_percent_json():
    value = None
    while 1:
        if value == None:
            cpuPercentDict = {
                "cpu_percent": None
            }
            cpuPercentArray = []
            value == 1
            break
        else: break

    cpuPercentDict["cpu_percent"] = str(psutil.cpu_percent())
    cpuPercentArray.append(cpuPercentDict)

    with open("cpu_percent_data.json", "r") as percent_file:
        percent_file_len = len(percent_file.readlines())
        percent_file.close()
    # print(cpu_file_len)

    if percent_file_len == 0:
        # print("file length is: " + str(percent_file_len))
        jsonFile = open("cpu_percent_data.json", "a")
        jsonString = json.dumps(cpuPercentDict, indent=2)
        jsonFile.write("[\n" + jsonString + "\n]")
        jsonFile.close()
    elif percent_file_len == 32: # Length is x = 10 items ((x-1)*3)+5
        with open("cpu_percent_data.json", "r+") as percent_file:
            percent_file.truncate()
            percent_file.close()
    else:
        # print("file length is: " + str(percent_file_len))
        fd=open("cpu_percent_data.json","r")
        d=fd.read()
        fd.close()
        m=d.split("\n")
        s="\n".join(m[:-1])
        fd=open("cpu_percent_data.json","w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
        # print("last line removed, file length is: " + str(percent_file_len))
        jsonString = json.dumps(cpuPercentDict, indent=2)
        jsonFile = open("cpu_percent_data.json", "a")
        jsonFile.write(",\n" + jsonString + "\n]")
        jsonFile.close()


# print("CPU Stats\n" + str(psutil.cpu_stats()))
def cpu_stats_json():
    value = None
    while 1:
        if value == None:
            cpuStatDict = {
                'ctx_switches': None, 
                'interrupts': None,
                'soft_interrupts': None,
                'syscalls': None,
                }
            cpuStatArray = []
            value == 1
            break
        else: break

    stats = str(psutil.cpu_stats())
    split_stats = stats.split("=")

    ctx_swtiches = str(split_stats[1])
    ctx_switches_split = ctx_swtiches.split(",")
    cpuStatDict["ctx_switches"] = ctx_switches_split[0]

    interrupts = str(split_stats[2])
    interrupts_split = interrupts.split(",")
    cpuStatDict["interrupts"] = interrupts_split[0]


    soft_interrupts = str(split_stats[3])
    soft_interrupts_split = soft_interrupts.split(",")
    cpuStatDict["soft_interrupts"] = soft_interrupts_split[0]


    syscalls = str(split_stats[4])
    edited_syscalls = syscalls.rstrip(syscalls[-1]) #removes last char
    cpuStatDict["syscalls"] = edited_syscalls

    cpuStatArray.append(cpuStatDict)


    with open("data.json", "r") as cpu_file:
        cpu_file_len = len(cpu_file.readlines())
        cpu_file.close()
    # print(cpu_file_len)

    if cpu_file_len == 0:
        # print("file length is: " + str(cpu_file_len))
        jsonFile = open("data.json", "a")
        jsonString = json.dumps(cpuStatDict, indent=2)
        jsonFile.write("[\n" + jsonString + "\n]")
        jsonFile.close()
    elif cpu_file_len == 62: # Length is x = 10 items (x*6)+2
        with open("data.json", "r+") as cpu_file:
            cpu_file.truncate()
            cpu_file.close()
    else:
        # print("file length is: " + str(cpu_file_len))
        fd=open("data.json","r")
        d=fd.read()
        fd.close()
        m=d.split("\n")
        s="\n".join(m[:-1])
        fd=open("data.json","w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
        # print("last line removed, file length is: " + str(cpu_file_len))
        jsonString = json.dumps(cpuStatDict, indent=2)
        jsonFile = open("data.json", "a")
        jsonFile.write(",\n" + jsonString + "\n]")
        jsonFile.close()
 

# print("CPU Frequency\n"  + str(psutil.cpu_freq()))




def cpu_freq_json():
    value = None
    while 1:
        if value == None:
            cpuFrequencyDict = {
                'current': None,
                'min': None,
                'max': None
                }
            cpuFrequencyArray = []
            value == 1
            break
        else: break


    freq = str(psutil.cpu_freq())

    split_freq = freq.split(",")
    current = split_freq[0]
    split_current = current.split("=")
    cpuFrequencyDict["current"] = split_current[1]

    minimum = split_freq[1]
    split_minimum = minimum.split("=")
    cpuFrequencyDict["min"] = split_minimum[1]


    maximum = split_freq[2]
    split_maximum = maximum.split("=")
    num_string = str(split_maximum[1])
    edited_num_string = num_string.rstrip(num_string[-1]) #removes last char
    cpuFrequencyDict["max"] = edited_num_string

    cpuFrequencyArray.append(cpuFrequencyDict)

    with open("cpu_frequency.json", "r") as freq_file:
        freq_file_len = len(freq_file.readlines())
        freq_file.close()
    # print(freq_file_len)

    if freq_file_len == 0:
        # print("file length is: " + str(freq_file_len))
        jsonFile = open("cpu_frequency.json", "a")
        jsonString = json.dumps(cpuFrequencyDict, indent=2)
        jsonFile.write("[\n" + jsonString + "\n]")
        jsonFile.close()
    elif freq_file_len == 52: # Length is x = 10 items ((x-1)*5)+7
        with open("cpu_frequency.json", "r+") as freq_file:
            freq_file.truncate()
            freq_file.close()
    else:
        # print("file length is: " + str(freq_file_len))
        fd=open("cpu_frequency.json","r")
        d=fd.read()
        fd.close()
        m=d.split("\n")
        s="\n".join(m[:-1])
        fd=open("cpu_frequency.json","w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()
        # print("last line removed, file length is: " + str(cpu_file_len))
        jsonString = json.dumps(cpuFrequencyDict, indent=2)
        jsonFile = open("cpu_frequency.json", "a")
        jsonFile.write(",\n" + jsonString + "\n]")
        jsonFile.close()