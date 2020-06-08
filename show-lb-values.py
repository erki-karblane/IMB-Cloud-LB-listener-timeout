import SoftLayer
from pprint import pprint

# Your load balancer UUID
uuid = 'enter your LB UUID here'
# mask to retrieve the load balancer's listeners and healthMonitors
_mask = "mask[listeners, healthMonitors]"

# Create the api client
client = SoftLayer.Client()
lbaas_service = client['Network_LBaaS_LoadBalancer']

try:
    # Retrieve a specific load balancer object
    details = lbaas_service.getLoadBalancer(uuid, mask=_mask)
    pprint(details)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve LBaaS details: %s, %s" % (e.faultCode, e.faultString))
