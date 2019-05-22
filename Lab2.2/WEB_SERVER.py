from flask import Flask, jsonify
import sys
import re
import glob
# import ipaddress
from ipaddress import IPv4Interface

def classify(s):
    """
    :param s: String to classify
    :return: Tuple of arguments
    """
    m = re.match('^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', s)

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
hosts = []

for current_file_name in glob.glob("C:\\PY_WORK\\*.txt"):

    with open(current_file_name) as f:
        for current_line in f:
            c = classify(current_line)
            if "ip" in c:
                ip_addresses.append(c)
            if "int" in c:
                interfaces.append(c)
            if "host" in c:
                hosts.append(c)

print(ip_addresses)
#print(interfaces)
a = hosts

print(a)

#####################################3
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Добрый день! Вы используете справочник хостов."

@app.route('/config')
def configs():
    return str(a)


#@app.route('/hostname/<name1>/<name2>')
#def hostname(name1, name2):
 #   return "Зафиксировано обращение к " + name1 + ", " + name2
#@app.route('/config/hostname')
#def config/hostname():
  #  return ip_addresses


if __name__ == '__main__':
     app.run(debug=True)