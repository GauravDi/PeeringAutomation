# PeeringAutomation

This script is written to automate the inbound policy on border device (Arista) to accept all prefixes of each fabric/customer AS.
Network organization's (Charter Communications - AS20115) fabric details are taken into json format and all prefixes of each connected autonomous system are parsed.
Jinja2 library is used to create a policy configuration template (to accept prefixes) and to put the values in it.
Arista eos python support api known as 'pyeapi' is used to connect to the Arista device and push all configurations over it.
