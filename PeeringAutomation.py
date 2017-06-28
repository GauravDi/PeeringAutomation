import pyeapi
from pprint import pprint
import jinja2
import requests

template = '''ip prefix-list {{name1}} seq {{num}} permit {{addr}}'''       # policy template configuration


def CharterCon(configs):

    node = pyeapi.connect_to('eos-spine1')           # connecting locally to border device with Arista eos api called 'pyeapi'
    node.config(configs)                             # pushing all policy configs

                                                     # To connect remotely, consider transport mechanism (https),
                                                     # host address, username, password and timeout duration.

def jsonpars(info):

    data = []
    data = info['data'][0]
    data1 = data['netixlan_set']
    a = 0
    name = []
    ip4 = []
    while a < len(data1):
        name.append(data1[a]['name'])                           # parsing 'AS name' and 'prefixes' from json data
        ip4.append(data1[a]['ipaddr4'])
        a = a + 1

    t = jinja2.Template(template)                                # declare policy configuration template
    b = 0
    con = []
    while b < len(name):
        out = t.render(name1=name[b], num=b + 1, addr=ip4[b])     # put parsed values into the template
        b = b + 1
        con.append(out)
    pprint(con)
    return con

def main():

    r = requests.get("https://www.peeringdb.com/api/net?asn=20115&depth=2")
    info = r.json()                                                             # extracting url data in json format

    conn = jsonpars(info)

    CharterCon(conn)

main()