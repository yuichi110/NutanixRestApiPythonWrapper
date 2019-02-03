from nutanix import NutanixRestApiClient

CLUSTER_IP = '10.149.27.41'
CLUSTER_USER = 'admin'
CLUSTER_PASSWORD = 'Nutanix/4u!'
session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)

# get cluster name
(success, name) = session.get_cluster_name()
print(name)

# create network rest_network. vlan 110
(success, taskuuid) = session.create_network('rest_network', 110)
print(taskuuid)
