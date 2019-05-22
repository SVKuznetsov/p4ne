from flask import Flask, jsonify
import sys
import re
import glob
# import ipaddress
from ipaddress import IPv4Interface

import re
import glob
# import ipaddress
from ipaddress import IPv4Interface
import pprint
from matplotlib import pyplot
from openpyxl import load_workbook

def classify(s):
    """
    :param s: String to classify
    :return: Tuple of arguments
    """
    m = re.match('^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', s)
   #print(m.group(0))
   # print(m.group(1))
   # print(m.group(2))
#classify(' ip address 10.0.1.2 255.255.255.0')
    if m:
        return {"ip":IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}

    m = re.match("^interface (.+)", s)
    if m:
        return {"int":m.group(1)}

    m = re.match("^hostname (.+)", s)
    if m:
        return {"host":m.group(1)}

    return ("UNCLASSIFIED")

ip_addresses = []
interfaces = []
hosts =  []

table = {}

for current_file_name in glob.glob("C:\\PY_WORK\\*.txt"):
    #("/Users/mk/Seafile/p4ne_training/config_files/*.txt"):
    with open(current_file_name) as f:
        table[current_file_name] = {}
        table[current_file_name]['interfaces'] = []
        table[current_file_name]['hostname'] = ""
        table[current_file_name]['ip'] = []
        for current_line in f:
            c = classify(current_line)
            if "ip" in c:
                ip_addresses.append(c)
                table[current_file_name]['ip'].append(c['ip'])
            if "int" in c:
                interfaces.append(c)
                table[current_file_name]['interfaces'].append(c['int'])
            if "host" in c:
                hosts.append(c)
                table[current_file_name]['hostname'] = c['host']

#pprint.pprint(table)

b = []
for x in table.keys():
    for y in table[x]['ip']:
        b.append((table[x]['hostname'],"\t", y))
        #print(b)#(table[x]['hostname'],"\t", y)
    #for y in table[x]['interfaces']:
        #print(table[x]['hostname'], "\t", y)

a = str(table)


#####################################3
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Добрый день! Вы используете справочник хостов."

@app.route('/config')
def configs():
    return (a)


@app.route('/hostname/<host_name>')
def hostname(host_name):
    s = []
    for x in b:
        if x[0] == host_name:
            s.append(x[2])
    return str(s)



if __name__ == '__main__':
     app.run(debug=True)