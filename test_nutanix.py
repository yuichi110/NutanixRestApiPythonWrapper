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

def test_cluster_all(session):
  test_get_cluster_info(session)
  test_get_cluster_name(session)
  test_get_hypervisor(session)
  test_get_version(session)
  test_get_name_servers(session)
  test_get_ntp_servers(session)
  test_block_serials(session)
  test_get_num_nodes(session)
  test_get_desired_redundancy_factor(session)
  test_get_current_redundancy_factor(session)

def test_get_cluster_info(session):
  result = session.get_cluster_info()
  print(result)

def test_get_cluster_name(session):
  result = session.get_cluster_name()
  print(result)

def test_get_hypervisor(session):
  result = session.get_hypervisor()
  print(result)

def test_get_version(session):
  result = session.get_version()
  print(result)

def test_get_name_servers(session):
  result = session.get_name_servers()
  print(result)

def test_get_ntp_servers(session):
  result = session.get_ntp_servers()
  print(result)

def test_block_serials(session):
  result = session.get_block_serials()
  print(result)

def test_get_num_nodes(session):
  result = session.get_num_nodes()
  print(result)

def test_get_desired_redundancy_factor(session):
  result = session.get_desired_redundancy_factor()
  print(result)

def test_get_current_redundancy_factor(session):
  result = session.get_current_redundancy_factor()
  print(result)

###
### Container
###

def test_container_all(session):
  #test_get_container_names(session)
  test_get_container_info(session)
  #test_create_container(session)
  #test_delete_container(session)
  #test_get_container_names(session)

def test_get_container_names(session):
  result = session.get_container_names()
  print(result)

def test_get_container_info(session):
  result = session.get_container_info('container')
  print(result)

def test_create_container():
  result = session.create_container('yuichi-container')
  print(result)

def test_delete_container(session):
  result = session.delete_container('yuichi-container')
  print(result)

###
### Network
###

def test_network_all(session):
  test_get_network_names(session)
  #test_get_network_info(session)
  #test_create_network(session)
  #test_create_network_managed(session)
  #test_is_network_used(session)
  #test_delete_network(session)

def test_get_network_names(session):

  result = session.get_network_names()
  print(result)

def test_get_network_info(session):
  result = session.get_network_info('Net-10.149')
  print(result)

def test_create_network(session):
  result = session.create_network('yuichi-network', 110)
  print(result)

def test_is_network_used(session):
  result = session.is_network_used('vlan.0')
  print(result)

def test_create_network_managed(session):
  result = session.create_network_managed('Net-10.149', 0, '10.149.0.0', 17, '10.149.0.1', [('10.149.27.50', '10.149.27.199')], '8.8.8.8')
  print(result)

def test_delete_network(session):
  result = session.delete_network('Net-10.149')
  print(result)


###
### VM
###

def test_vm_all(session):
  #test_get_vm_names(session)
  #test_create_vm_from_image(session)
  test_get_vm_info(session)

def test_get_vm_names(session):
  result = session.get_vm_names()
  print(result)

def test_get_vm_info(session):
  result = session.get_vm_info('rest_test')
  print(result)

def test_create_vm_from_image(session):
  result = session.create_vm_from_image('rest_test', 2048, 1, 2, 'REST_CENT7_IMG', 'REST_NETWORK')
  print(result)


###
### vDisk
###

def test_get_vm_disks(session):
  VM = 'REST_TEST_VM'
  result = session.get_vm_disks(VM)
  print(result)


###
### Image
###

def test_image_all(session):
  #test_get_image_names(session)
  #test_upload_image(session)
  #test_create_image_from_vm_vdisk(session)
  test_delete_image(session)

def test_get_image_names(session):
  result = session.get_image_names()
  print(result)

def test_upload_image(session):
  result = session.upload_image('nfs://10.149.245.50/Public/bootcamp/centos7_min_raw', 'container', 'cent7-image-rest')
  print(result)

def test_create_image_from_vm_vdisk(session):
  result = session.create_image_from_vm_vdisk('rest_test', 'scsi.0', 'container', 'cent7-image-rest2')
  print(result)

def test_delete_image(session):
  result = session.delete_image('cent7-image-rest2')
  print(result)

###
### Task
###

def test_task_all(session):
  #test_upload_image(session)
  #test_get_task_status(session)
  test_get_tasks_status(session)

def test_get_task_status(session):
  TASK_UUID = 'f25cbedf-ca76-491a-aa20-e1fe77a92f42'
  result = session.get_task_status(TASK_UUID)
  print(result)

def test_get_tasks_status(session):
  result = session.get_tasks_status()
  print(result)

if __name__ == '__main__':
  logger = NutanixRestApiClient.create_logger('test_rest.log', logging.DEBUG)
  session = NutanixRestApiClient(CLUSTER_IP, CLUSTER_USER, CLUSTER_PASSWORD, logger)
  test_upload_image(session)
