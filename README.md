# IMB-Cloud-LB-listener-timeout
This is a Python3 script to change IBM Cloud loadbalancer timeout settings
Your goint to need to have Softplayer imported to Your python, and a IBM vpn username along with your classical infrastructure API key with currect user rights. To use the correct credentials:

Set an api username and apikey as following for each example in case you don't have a ~/.softlayer file configured in your environment.

    client = SoftLayer.Client(username='set me', api_key='set me')
   
Or like this:
https://github.com/softlayer/softlayer-python/blob/master/docs/config_file.rst#id1


The script itself:

    import SoftLayer
    
    from pprint import pprint

    # Your load balancer UUID
    uuid = 'Your load balancer UUID or UUI if You are using SLCLI'

    # New protocols to add
    protocolConfigurations = [
        {
            "listenerUuid": "UUID of the listener or UUID of the Pool1 from SLCLI",
            "serverTimeout": 50,
            "clientTimeout": 50
        },
        {
            "listenerUuid": "UUID of the listener or UUID of the Pool2 from SLCLI",
            "serverTimeout": 50,
            "clientTimeout": 50
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
---------------------------------------------------
How to get information regarding your current setup:

  Using SLCLI:

    slcli loadbal list
    
        slcli loadbal detail id
        The ID here is a 6 ficure number
   
The problem with the slcli tool is that this does not show or change the timeout settings. You need pyhton scripts.
To see the current values, use the python script below:
   
    import SoftLayer

    from pprint import pprint

    # Your load balancer UUID
    uuid = 'UUID of Your loadbalancer'
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
-------------------------------------------------------------
How to add a L7 rule to a load balancer (listener)

import SoftLayer
from pprint import pprint

# UUID of the HTTP listener
listener_uuid = "18996791-9e06-436b-bcf8-ba4a849af723"

# Bulk rules configuration
policies_rules = [
    {
        "l7Policy": {
            "name": "redirect-to-HTTPS",
            "action": "REDIRECT_HTTPS",
            "priority": 101,
# Redirect the http to https listener UUID
            "redirectUrl": "fcd21b75-236b-41e5-ac10-db6e63d75078"
        }
    }
]

client = SoftLayer.Client()
networkLBaaSL7PolicyService = client['SoftLayer_Network_LBaaS_L7Policy']

try:
    result = networkLBaaSL7PolicyService.addL7Policies(listener_uuid, policies_rules)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to addL7Policies: %s, %s " % (e.faultCode, e.faultString))

