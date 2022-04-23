from matplotlib import pyplot as plt
import requests
import json

import psutil


URL = "http://127.0.0.1:8000/CpuDataApi/"


def get_data():
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    # print(data)

    corelist = []
    cpulist = []
    ramlist = []
    id = []
    n = 1

    for dic in data:

        core = int(float(dic["core3"]))
        cpu = int(float(dic["cpuSpeed"])) * 10
        ram = int(float(dic["ramUsage"]))

        corelist.append(core)
        cpulist.append(cpu)
        ramlist.append(ram)

        id.append(n)
        n += 1

    plt.plot(id, corelist)
    plt.plot(id, ramlist)
    plt.plot(id, cpulist)
    plt.legend(["Cpu usage", "Ram usage", "Cpu Speed"])

    plt.title("CPU and RAM usage")
    plt.xlabel("Over time -->")
    plt.ylabel("Percentage")
    plt.show()


def post_data():

    for index in range(10):

        cpuArray = psutil.cpu_percent(interval=1, percpu=True)
        cpuFreq = psutil.cpu_freq()
        ram = psutil.virtual_memory()

        data = {
            "core1": str(cpuArray[0]),
            "core2": str(cpuArray[1]),
            "core3": str(cpuArray[2]),
            "core4": str(cpuArray[3]),
            "cpuSpeed": str(int(cpuFreq.current) / 1000),
            "ramUsage": str(ram.percent),
        }

        json_data = json.dumps(data)
        r = requests.post(url=URL, data=json_data)
        data = r.json()
        print(data)


# post current cpu data
post_data()

input = input()
# all data
# list of objects
get_data()
