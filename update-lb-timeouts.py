import SoftLayer
from pprint import pprint

# Your load balancer UUID
uuid = '28bb4666-b263-4bc0-a0e7-7baec3e6-enter your lb UUID here'

# New protocols to add
protocolConfigurations = [
    {
        "listenerUuid": "0dffc0bc-0cfb-4797-aec8-enter your listener UUID here",
        "serverTimeout": 300,
        "clientTimeout": 80
    },
    {
        "listenerUuid": "36398819-5e0b-4536-enter your second linterner UUID here",
        "serverTimeout": 300,
        "clientTimeout": 80
    }
]

# Create the api client
client = SoftLayer.Client()
listener_service = client['Network_LBaaS_Listener']

_mask = "mask[listeners]"

try:
    response = listener_service.updateLoadBalancerProtocols(uuid, protocolConfigurations, mask=_mask)
    pprint(response)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to add protocols: %s, %s" % (e.faultCode, e.faultString))
