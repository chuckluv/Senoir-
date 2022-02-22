import json
from sre_parse import State
from textwrap import indent
from flask import Flask, render_template, url_for
from subprocess import check_output
import psutil # before running pip install psutil

print("CPU Percent\n" + str(psutil.cpu_percent()))
cpuPercentDict = {
    "cpu_percent": None
}
cpuPercentArray = []

# start loop
cpuPercentDict["cpu_percent"] = str(psutil.cpu_percent())
cpuPercentArray.append(cpuPercentDict)
# end loop
for x in cpuPercentArray:
    print(cpuPercentDict)


print("CPU Stats\n" + str(psutil.cpu_stats()))
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
    # end loop\

    for x in cpuStatArray:
        print(cpuStatArray)

    open_bracket = None
    while 1:
        if open_bracket == None:
            jsonFile = open("data.json", "a")
            jsonString = json.dumps(cpuStatDict, indent=2)
            jsonFile.write("[\n" + jsonString + "]\n")
            jsonFile.close()
            open_bracket == 1
            break
        else: break
    jsonString = json.dumps(cpuStatDict, indent=2)
    jsonFile = open("data.json", "a")
    jsonFile.write(jsonString + ",\n]")
    jsonFile.close()



print("CPU Frequency\n"  + str(psutil.cpu_freq()))
cpuFrequencyDict = {
    'current': None,
    'min': None,
    'max': None
}

cpuFrequencyArray = []

# start loop
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
# end loop

for x in cpuFrequencyArray:
    print(cpuFrequencyArray)