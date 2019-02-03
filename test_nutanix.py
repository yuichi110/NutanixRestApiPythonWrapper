'''
Test module for nutanix.py (Python REST API wrapper)

Author: Yuichi Ito
Email: yuichi.ito@nutanix.com
'''

if __name__ != '__main__':
  print("Please don't import module \"test_nutanix\". It is only for testing.")
  print('Abort.')
  exit(1)

import logging
TEST_LOG_NAME = 'test.log'
TEST_LOG_LEVEL = logging.DEBUG
TEST_LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s :%(message)s'


from nutanix import NutanixRestApiClient

# PARAM FOR SESSION
CLUSTER_IP = '10.149.27.41'
CLUSTER_USER = 'admin'
CLUSTER_PASSWORD = 'Nutanix/4u!'

###
### Login(init)
###

def test_login():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)


###
### Cluster
###

def test_cluster_all():
  test_get_cluster_info()
  test_get_cluster_name()
  test_get_hypervisor()
  test_get_version()
  test_get_name_servers()
  test_get_ntp_servers()
  test_block_serials()
  test_get_num_nodes()
  test_get_desired_redundancy_factor()
  test_get_current_redundancy_factor()

def test_get_cluster_info():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_cluster_info()
  print(result)

def test_get_cluster_name():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_cluster_name()
  print(result)

def test_get_hypervisor():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_hypervisor()
  print(result)

def test_get_version():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_version()
  print(result)

def test_get_name_servers():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_name_servers()
  print(result)

def test_get_ntp_servers():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_ntp_servers()
  print(result)

def test_block_serials():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_block_serials()
  print(result)

def test_get_num_nodes():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_num_nodes()
  print(result)

def test_get_desired_redundancy_factor():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_desired_redundancy_factor()
  print(result)

def test_get_current_redundancy_factor():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_current_redundancy_factor()
  print(result)

###
### Container
###

def test_container_all():
  #test_get_container_names()
  test_get_container_info()
  #test_create_container()
  #test_delete_container()
  #test_get_container_names()

def test_get_container_names():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_container_names()
  print(result)

def test_get_container_info():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_container_info('container')
  print(result)

def test_create_container():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.create_container('yuichi-container')
  print(result)

def test_delete_container():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.delete_container('yuichi-container')
  print(result)

###
### Network
###

def test_network_all():
  #test_get_network_names()
  #test_get_network_info()
  #test_create_network()
  test_create_network_managed()
  #test_is_network_used()
  #test_delete_network()

def test_get_network_names():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_network_names()
  print(result)

def test_get_network_info():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_network_info('Net-10.149')
  print(result)

def test_create_network():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.create_network('yuichi-network', 110)
  print(result)

def test_is_network_used():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.is_network_used('vlan.0')
  print(result)

def test_create_network_managed():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.create_network_managed('Net-10.149', 0, '10.149.0.0', 17, '10.149.0.1', [('10.149.27.50', '10.149.27.199')], '8.8.8.8')
  print(result)

def test_delete_network():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.delete_network('Net-10.149')
  print(result)


###
### VM
###

def test_vm_all():
  #test_get_vm_names()
  #test_create_vm_from_image()
  test_get_vm_info()

def test_get_vm_names():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_vm_names()
  print(result)

def test_get_vm_info():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_vm_info('rest_test')
  print(result)

def test_create_vm_from_image():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.create_vm_from_image('rest_test', 2048, 1, 2, 'REST_CENT7_IMG', 'REST_NETWORK')
  print(result)


###
### vDisk
###

def test_get_vm_disks():
  VM = 'REST_TEST_VM'
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_vm_disks(VM)
  print(result)


###
### Image
###

def test_image_all():
  #test_get_image_names()
  #test_upload_image()
  #test_create_image_from_vm_vdisk()
  test_delete_image()

def test_get_image_names():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_image_names()
  print(result)

def test_upload_image():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.upload_image('nfs://10.149.245.50/Public/bootcamp/centos7_min_raw', 'container', 'cent7-image-rest')
  print(result)

def test_create_image_from_vm_vdisk():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.create_image_from_vm_vdisk('rest_test', 'scsi.0', 'container', 'cent7-image-rest2')
  print(result)

def test_delete_image():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.delete_image('cent7-image-rest2')
  print(result)

###
### Task
###

def test_task_all():
  #test_upload_image()
  #test_get_task_status()
  test_get_tasks_status()

def test_get_task_status():
  TASK_UUID = 'f25cbedf-ca76-491a-aa20-e1fe77a92f42'
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_task_status(TASK_UUID)
  print(result)

def test_get_tasks_status():
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD)
  result = session.get_tasks_status()
  print(result)

if __name__ == '__main__':
  test_task_all()
