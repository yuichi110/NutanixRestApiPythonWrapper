'''
Python wrapper for Nutanix REST API.
Version 0.01

Author: Yuichi Ito
Email: yuichi.ito@nutanix.com
'''

import requests
import json
import traceback
import logging

import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class NutanixRestApiClient:
  def __init__(self, ip, username, password, timeout_connection=2, timeout_read=5):
    TIMEOUT = (timeout_connection, timeout_read)

    # Test IP and Port reachability
    is_port_open = True
    import socket
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(timeout_connection) # seconds
      s.connect((ip, 9440))
      s.shutdown(2)
    except Exception as e:
      is_port_open = False
    if not is_port_open:
      raise Exception('Unable to connect Nutanix Cluster "{}". Please check ip and port.'.format(ip))

    # Make session
    session = requests.Session()
    session.auth = (username, password)
    session.verify = False                              
    session.headers.update({'Content-Type': 'application/json; charset=utf-8'})

    # Test session
    is_requests_ok = True
    url = 'https://{}:9440/PrismGateway/services/rest/v1/cluster'.format(ip)
    try:
      resp = session.get(url, timeout=TIMEOUT)
    except:
      is_requests_ok = False
    if not is_requests_ok:
      raise Exception('Able to access. But unexpected error happens. Please check server status.')
    if not resp.ok:
      raise Exception('Able to access. But unable to get cluster info. Please check your credential.')

    ###
    ### Make CRUD utility private methods with closure.
    ### To avoid being modifyied session and ip etc from outside of instance.
    ###

    # API v0.8

    def get_v08(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.get('https://{}:9440/api/nutanix/v0.8{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._get_v08 = get_v08

    def post_v08(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.post('https://{}:9440/api/nutanix/v0.8{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._post_v08 = post_v08

    def put_v08(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.put('https://{}:9440/api/nutanix/v0.8{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._put_v08 = put_v08

    def delete_v08(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.delete('https://{}:9440/api/nutanix/v0.8{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      try:
        return response.json()
      except:
        return {}
    self._delete_v08 = delete_v08


    # API v1

    def get_v1(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.get('https://{}:9440/api/nutanix/v1{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._get_v1 = get_v1

    def post_v1(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.post('https://{}:9440/api/nutanix/v1{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._post_v1 = post_v1

    def put_v1(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.put('https://{}:9440/api/nutanix/v1{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._put_v1 = put_v1

    def delete_v1(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.delete('https://{}:9440/api/nutanix/v1{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      try:
        return response.json()
      except:
        return {}
    self._delete_v1 = delete_v1


    # API v2

    def get_v2(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.get('https://{}:9440/api/nutanix/v2.0{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._get_v2 = get_v2

    def post_v2(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.post('https://{}:9440/api/nutanix/v2.0{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._post_v2 = post_v2

    def put_v2(url, body_dict, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.put('https://{}:9440/api/nutanix/v2.0{}'.format(ip, url), data=json.dumps(body_dict), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))
      return response.json()
    self._put_v2 = put_v2

    def delete_v2(url, error_dict):
      if not url.startswith('/'): url = '/' + url
      response = session.delete('https://{}:9440/api/nutanix/v2.0{}'.format(ip, url), timeout=TIMEOUT)
      if not response.ok:
        error_dict['method'] = response.request.method
        error_dict['url'] = response.request.url
        error_dict['code'] = response.status_code
        error_dict['text'] = response.text
        raise IntendedException('Receive unexpected response code "{}".'.format(response.status_code))

      # sometimes get nothing.
      try:
        return response.json()
      except:
        return {}
    self._delete_v2 = delete_v2


    # Error handling

    def handle_error(error, error_dict):
      if not isinstance(error, IntendedException):
        error_dict['stacktrace'] = traceback.format_exc()
      error_dict['error'] = str(error)
    self._handle_error = handle_error


  ###
  ### Cluster Operation
  ###

  def get_cluster_info(self):
    error_dict = {}
    try:
      response_dict = self._get_v1('/cluster/', error_dict)
      return_dict = {
        # Basic
        'uuid' : response_dict['uuid'],
        'name' : response_dict['name'],
        'timezone' : response_dict['timezone'],
        'is_lts' : response_dict['isLTS'],
        'version' : response_dict['version'],
        'version_ncc' : response_dict['nccVersion'],

        # RF
        'current_redundancy_factor' : response_dict['clusterRedundancyState']['currentRedundancyFactor'],
        'desired_redundancy_factor' : response_dict['clusterRedundancyState']['desiredRedundancyFactor'],

        # Network
        'ip_external' : response_dict['clusterExternalIPAddress'],
        'ip_iscsi' : response_dict['clusterExternalDataServicesIPAddress'],
        'network_external' : response_dict['externalSubnet'],
        'network_internal' : response_dict['internalSubnet'],
        'nfs_whitelists' : response_dict['globalNfsWhiteList'],

        # Node and Block
        'num_nodes' : response_dict['numNodes'],
        'block_serials' : response_dict['blockSerials'],
        'num_blocks' : len(response_dict['blockSerials']),

        # Servers
        'name_servers' : response_dict['nameServers'],
        'ntp_servers' : response_dict['ntpServers'],
        'smtp_server' : '' if response_dict['smtpServer'] is None else response_dict['smtpServer'],

        # Storage
        'storage_type' : response_dict['storageType'],
      }

      hypervisors = response_dict['hypervisorTypes']
      if len(hypervisors) == 1:
        return_dict['hypervisor'] = hypervisors[0]
        if return_dict['hypervisor'] == 'kKvm':
          return_dict['hypervisor'] = 'AHV'
      else:
        # needs update here
        return_dict['hypervisor'] = 'unknown'

      return (True, return_dict)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)

  def get_cluster_name(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['name'])
    return (success, dict)

  def change_cluster_name(self):
    return {'error':'Error: Not supported now'}

  def get_hypervisor(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['hypervisor'])
    return (success, dict)

  def get_version(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['version'])
    return (success, dict)

  def get_name_servers(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['name_servers'])
    return (success, dict)

  def get_ntp_servers(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['ntp_servers'])
    return (success, dict)

  def get_block_serials(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['block_serials'])
    return (success, dict)

  def get_num_nodes(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['num_nodes'])
    return (success, dict)

  def get_desired_redundancy_factor(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['desired_redundancy_factor'])
    return (success, dict)

  def get_current_redundancy_factor(self):
    (success, dict) = self.get_cluster_info()
    if success:
      return (success, dict['current_redundancy_factor'])
    return (success, dict)


  ###
  ### Storagepool Operation
  ###

  def get_storagepool_names(self):
    error_dict = {}
    try:
      response_dict = self._get_v1('/storage_pools/', error_dict)
      storagepools = []
      for storagepool in response_dict['entities']:
        storagepools.append(storagepool['name'])
      return (True, storagepools)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  ###
  ### Container Operation
  ###

  def get_container_names(self):
    error_dict = {}
    try:
      response_dict = self._get_v1('/containers/', error_dict)
      container_names = []
      for cont in response_dict['entities']:
        container_names.append(cont['name'])
      return (True, container_names)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def get_container_info(self, name):
    error_dict = {}
    try:
      response_dict = self._get_v1('/containers/', error_dict)
      container_info = {}
      for cont in response_dict['entities']:
        if cont['name'] != name:
          continue
        container_info = {
          'uuid':cont['containerUuid'],
          'id':cont['id'],
          'storagepool_uuid':cont['storagePoolUuid'],
          'usage':cont['usageStats']['storage.usage_bytes']
        }
        break  
      if len(container_info) == 0:
        raise IntendedException('Error. Unable to find container "{}"'.format(name))
      return (True, container_info)
      
    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)

  def create_container(self, container_name, storagepool_name=''):
    error_dict = {}
    try:
      # Get storage pool uuid.
      response_dict = self._get_v1('/storage_pools/', error_dict)
      storagepool_dict = {}
      for storagepool in response_dict['entities']:
        storagepool_dict[storagepool['name']] = storagepool['storagePoolUuid']
      storagepool_uuid = ''
      if storagepool_name == '':
        if len(storagepool_dict) != 1:
          raise IntendedException('Error. Needs to provide storagepool name if having 2+ pools.')
        storagepool_uuid = storagepool_dict.popitem()[1]
      else:
        if storagepool_name not in storagepool_dict:
          raise IntendedException('Error. Storagepool name "{}" doesn\'t exist.'.format(storagepool_name))
        storagepool_uuid = storagepool_dict[storagepool_name]

      # Create container
      body_dict = {
        "id": None,
        "name": container_name,
        "storagePoolId": storagepool_uuid,
        "totalExplicitReservedCapacity": 0,
        "advertisedCapacity": None,
        "compressionEnabled": True,
        "compressionDelayInSecs": 0,
        "fingerPrintOnWrite": "OFF",
        "onDiskDedup": "OFF"
      }
      response_dict = self._post_v1('/containers/', body_dict, error_dict)
      return (True, response_dict['value'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)

  def update_container(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def delete_container(self, name):
    error_dict = {}
    try:
      # Get uuid from name
      response_dict = self._get_v1('/containers/', error_dict)
      container_uuid = ''
      for cont in response_dict['entities']:
        if cont['name'] == name:
          container_uuid = cont['containerUuid']
          break
      if container_uuid == '':
        raise IntendedException('Error. Unable to find container "{}"'.format(name))

      # Delete
      response_dict = self._delete_v1('/containers/{}'.format(container_uuid), error_dict)
      return (True, response_dict['value'])
      
    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  ###
  ### Network Operation
  ###

  def get_network_names(self):
    error_dict = {}
    try:
      response_dict = self._get_v2('/networks/', error_dict)
      network_names = []
      for network in response_dict['entities']:
        network_names.append(network['name'])
      return (True, network_names)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def get_network_info(self, name):
    error_dict = {}
    try:
      response_dict = self._get_v2('/networks/', error_dict)
      network_info = {}
      for network in response_dict['entities']:
        if name != network['name']:
          continue
        network_info = {
          'name' : network['name'],
          'uuid' : network['uuid'],
          'vlan' : network['vlan_id'],
          'managed' : False
        }
        if 'network_address' in network['ip_config']:
          network_info['managed'] = True
          network_info['managed_address'] = network['ip_config']['network_address']
          network_info['managed_prefix'] = network['ip_config']['prefix_length']
          network_info['managed_gateway'] = network['ip_config']['default_gateway']
          network_info['managed_dhcp_address'] = network['ip_config']['dhcp_server_address']
          network_info['managed_dhcp_options'] = network['ip_config']['dhcp_options']
          pools = []
          for pool in network['ip_config']['pool']:
            words = pool['range'].split(' ')
            pools.append((words[0], words[1]))
          network_info['managed_pools'] = pools
        break
      if network_info == {}:
        raise IntendedException('Error. Unable to find network "{}"'.format(name))
      return (True, network_info)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def create_network(self, name, vlan):
    error_dict = {}
    try:
      body_dict = {
        'name' : name,
        'vlan_id' : str(vlan)
      }
      response_dict = self._post_v2('/networks/', body_dict, error_dict)
      return (True, response_dict['network_uuid'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def create_network_managed(self, name, vlan, network_address, prefix, gateway, pools, dns=''):
    error_dict = {}
    try:      
      body_dict = {
        'name' : name,
        'vlan_id' : str(vlan),
        'ip_config': {
          'dhcp_options': {
            'domain_name_servers': dns,
          },
          'network_address': network_address,
          'prefix_length': str(prefix),
          'default_gateway': gateway,
          "pool": []
        }
      }
      for (from_ip, to_ip) in pools:
        entity = {'range' : '{} {}'.format(from_ip, to_ip)}
        body_dict['ip_config']['pool'].append(entity)

      response_dict = self._post_v2('/networks/', body_dict, error_dict)
      return (True, response_dict['network_uuid'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def is_network_used(self, name):
    error_dict = {}
    try:
      # Get uuid
      response_dict = self._get_v2('/networks/', error_dict)
      network_uuid = ''
      for network in response_dict['entities']:
        if network['name'] == name:
          network_uuid = network['uuid']
          break
      if network_uuid == '':
        raise IntendedException('Error. Unable to find network "{}"'.format(name))

      # Check all VMs whether using this network or not.
      response_dict = self._get_v2('/vms/?include_vm_nic_config=true', error_dict)
      is_used = False
      for vm in response_dict['entities']:
        for nic in vm['vm_nics']:
          if network_uuid == nic['network_uuid']:
            is_used = True
            break
        if is_used:
          break
      return (True, is_used)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def delete_network(self, name):
    error_dict = {}
    try:
      # Get uuid
      response_dict = self._get_v2('/networks/', error_dict)
      network_uuid = ''
      for network in response_dict['entities']:
        if network['name'] == name:
          network_uuid = network['uuid']
          break
      if network_uuid == '':
        raise IntendedException('Error. Unable to find network "{}"'.format(name))

      # Delete
      response_dict = self._delete_v2('/networks/{}'.format(network_uuid), error_dict)
      return (True, None)
      
    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def update_network():
    return (False, {'error':'Error. Not supported now.'})


  ###
  ### VM Operation
  ###

  def get_vm_names(self):
    error_dict = {}
    try:
      response_dict = self._get_v2('/vms/', error_dict)
      vm_names = []
      for vm in response_dict['entities']:
        vm_names.append(vm['name'])
      return (True, vm_names)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)

  def get_vm_info(self, name):
    error_dict = {}
    try:
      response_dict = self._get_v2('/vms/?include_vm_disk_config=true&include_vm_nic_config=true', error_dict)
      vm_info = {}
      for vm in response_dict['entities']:
        if vm['name'] != name:
          continue
        vm_info = {
          'name' : vm['name'],
          'uuid' : vm['uuid'],
          'memory_mb' : vm['memory_mb'],
          'num_vcpus' : vm['num_vcpus'],
          'num_cores' : vm['num_cores_per_vcpu'],
          'power_state' : vm['power_state'],
          'timezone' : vm['timezone'],
          'is_agent' : vm['vm_features'].get('AGENT_VM', False)
        }

        disks = []
        for disk in vm['vm_disk_info']:
          disk_info = {
            'bus' : disk['disk_address']['device_bus'],
            'label' : disk['disk_address']['disk_label'],
            'is_cdrom' : disk['is_cdrom'],
            'is_flashmode' : disk['flash_mode_enabled'],
            'is_empty' : disk['is_empty'],
            'vmdisk_uuid' : disk['disk_address'].get('vmdisk_uuid', ''),
            'container_uuid' : disk.get('storage_container_uuid', ''),
            'size' : disk.get('size', 0)
          }
          disks.append(disk_info)
        vm_info['disks'] = disks

        nics = []
        for nic in vm['vm_nics']:
          nic_info = {
            'mac_address' : nic['mac_address'],
            'network_uuid' : nic['network_uuid'],
            'is_connected' : nic['is_connected']
          }
        vm_info['nics'] = nics
        break
      if vm_info == {}:
        raise IntendedException('Error. Unable to find vm "{}"'.format(name))
      return (True, vm_info)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)

  def clone_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def create_vm_new(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def create_vm_from_image(self, name, memory_mb, num_vcpus, num_cores, image_name, network_name, ip_address=''):
    error_dict = {}
    try:
      # image uuid
      response_dict = self._get_v2('/images/', error_dict)
      vmdisk_uuid = ''
      vmdisk_size = 0
      for image in response_dict['entities']:
        if image['name'] == image_name:
          vmdisk_uuid = image['vm_disk_id']
          vmdisk_size = image['vm_disk_size']
          break
      if vmdisk_uuid == '':
        raise IntendedException('Error. Unable to find image "{}"'.format(image_name))

      # network uuid
      response_dict = self._get_v2('/networks/', error_dict)
      network_uuid = ''
      for network in response_dict['entities']:
        if network['name'] == network_name:
          network_uuid = network['uuid']
          break
      if network_uuid == '':
        raise IntendedException('Error. Unable to find network "{}"'.format(name))

      # create vm with image_uuid and network_uuid
      body_dict = {
        "name": name,
        "memory_mb": memory_mb,
        "num_vcpus": num_vcpus,
        "description": "",
        "num_cores_per_vcpu": num_cores,
        "vm_disks": [
          {
            "is_cdrom": True,
            "is_empty": True,
            "disk_address": {
              "device_bus": "ide"
            }
          },
          {
            "is_cdrom": False,
            "disk_address": {
              "device_bus": "scsi"
            },
            "vm_disk_clone": {
              "disk_address": {
                "vmdisk_uuid": vmdisk_uuid
              },
              "minimum_size": vmdisk_size
            }
          }
        ],
        "vm_nics": [
          {
            "network_uuid": network_uuid,
            "requested_ip_address": ip_address
          }
        ],
        "affinity": None,
        "vm_features": {
          "AGENT_VM": False
        }
      }
      if ip_address == '':
        del body_dict['vm_nics'][0]['requested_ip_address']
      response_dict = self._post_v2('/vms/', body_dict, error_dict)
      return (True, response_dict['task_uuid'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def update_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def delete_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def poweron_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def poweroff_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def shutdown_vm(self, name):
    return (False, {'error':'Error. Not supported now.'})

  def snapshot_vm(self, vm_name, snapshot_name):
    return (False, {'error':'Error. Not supported now.'})


  ###
  ### Vdisk Operation
  ###

  def get_vm_disks(self, vm_name):
    error_dict = {}
    try:
      response_dict = self._get_v2('/vms/?include_vm_disk_config=true', error_dict)
      for vm in response_dict['entities']:
        if vm['name'] != vm_name:
          continue
        vdisks = []
        for vdisk in vm['vm_disk_info']:
          if vdisk['is_cdrom']:
            continue
          vdisks.append(vdisk['disk_address']['disk_label'])
        return (True, vdisks)
      raise IntendedException('Error. Unable to find the vm "{}"'.format(name))

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  ###
  ### Image Operation
  ###

  def get_image_names(self):
    error_dict = {}
    try:
      response_dict = self._get_v08('/images/', error_dict)
      image_names = []
      for image in response_dict['entities']:
        image_names.append(image['name'])
      return (True, image_names)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def upload_image(self, file_url, target_container, image_name):
    error_dict = {}
    try:
      # Get container UUID
      response_dict = self._get_v1('/containers/', error_dict)
      target_container_uuid = ''
      for cont in response_dict['entities']:
        if cont['name'] == target_container:
          target_container_uuid = cont['containerUuid']
          break
      if target_container_uuid == '':
        raise IntendedException('Unable to find container "{}"'.format(target_container))

      # Upload
      is_iso = file_url.lower().endswith('.iso')
      image_type = 'ISO_IMAGE' if is_iso else 'DISK_IMAGE'
      body_dict = {
        "name": image_name,
        "annotation": "",
        "imageType": image_type,
        "imageImportSpec": {
          "containerUuid": target_container_uuid,
          "url": file_url,
        }
      }
      response_dict = self._post_v08('/images/', body_dict, error_dict)
      return (True, response_dict['taskUuid'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def create_image_from_vm_vdisk(self, vm_name, vm_disk, target_container, image_name):
    error_dict = {}
    try:
      # Get vdisk_uuid and source_container_uuid
      response_dict = self._get_v2('/vms/?include_vm_disk_config=true', error_dict)
      vdisk_uuid = ''
      source_container_uuid = ''
      for vm in response_dict['entities']:
        if vm['name'] != vm_name:
          continue
        for vdisk in vm['vm_disk_info']:
          if vdisk['disk_address']['disk_label'] != vm_disk:
            continue
          vdisk_uuid = vdisk['disk_address']['vmdisk_uuid']
          source_container_uuid = vdisk['storage_container_uuid']
          break
        break
      if vdisk_uuid == '':
        raise Exception('Error: Unable to find VM "{}" which has vDisk "{}"'.format(vm_name, vm_disk))

      # Get souce_container_name and target_container_uuid
      response_dict = self._get_v1('/containers/', error_dict)
      source_container_name = ''
      target_container_uuid = ''
      for cont in response_dict['entities']:
        if cont['containerUuid'] == source_container_uuid:
          source_container_name = cont['name']
        if cont['name'] == target_container:
          target_container_uuid = cont['containerUuid']
      if source_container_name == '':
        raise IntendedException('Error: Unable to find source container name from uuid="{}".'.format(source_container_uuid))
      if target_container_uuid == '':
        raise IntendedException('Error: Unable to find container "{}"'.format(target_container))

      # Upload image from VM vDisk
      nfs_url = 'nfs://127.0.0.1/{}/.acropolis/vmdisk/{}'.format(source_container_name, vdisk_uuid)
      body_dict = {
        "name": image_name,
        "annotation": "",
        "imageType": 'DISK_IMAGE',
        "imageImportSpec": {
          "containerUuid": target_container_uuid,
          "url": nfs_url,
        }
      }
      response_dict = self._post_v08('/images/', body_dict, error_dict)
      return (True, response_dict['taskUuid'])
      
    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def delete_image(self, name):
    error_dict = {}
    try:
      # Get image UUID
      response_dict = self._get_v08('/images/', error_dict)
      image_uuid = ''
      for image in response_dict['entities']:
        if image['name'] == name:
          image_uuid = image['uuid']
          break
      if image_uuid == '':
        raise IntendedException('Error: Unable to find image "{}"'.format(name))

      # Delete
      response_dict = self._delete_v08('/images/{}'.format(image_uuid), error_dict)
      return (True, response_dict['taskUuid'])

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  ###
  ### Task Operation
  ###

  def get_tasks_status(self):
    error_dict = {}
    try:
      response_dict = self._get_v08('/tasks/?includeCompleted=false', error_dict)
      task_list = []
      for entity in response_dict['entities']:
        entity_dict = {
          'uuid': entity['uuid'],
          'method': entity['metaRequest']['methodName'],
          'percent': entity.get('percentageComplete', 0),
          'status': entity['progressStatus'],
        }
        task_list.append(entity_dict)
      return (True, task_list)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


  def get_task_status(self, task_uuid):
    error_dict = {}
    try:
      response_dict = self._get_v08('/tasks/{}'.format(task_uuid), error_dict)
      return_dict = {
        'uuid': response_dict['uuid'],
        'method': response_dict['metaRequest']['methodName'],
        'percent': response_dict.get('percentageComplete', 0),
        'status': response_dict['progressStatus'],
      }
      return (True, return_dict)

    except Exception as exception:
      self._handle_error(exception, error_dict)
      return (False, error_dict)


###
### Exception Class
###

class IntendedException(Exception):
  pass
