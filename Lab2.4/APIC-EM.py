import requests,json,pprint
from flask import Flask
from flask import render_template, jsonify

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

def topology(ticket):
    url = "https://devnetapi.cisco.com/sandbox/apic_em/api/v1/topology/physical-topology"
    header = {"content-type": "application/json", "X-Auth-Token":ticket}
    responce = requests.get(url, headers=header, verify=False)

    pprint.pprint(responce.json())
    return responce.json()

#####################################3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology2():
    ticket = new_ticket()
    return jsonify(topology(ticket)['response'])



if __name__ == '__main__':

    # pprint.pprint(topology(ticket))
    app.run(debug=True)
