# libpve

Python interface for interacting with proxmox.

## Getting started

```python
import libpve

pve = libpve.Shell()
pve.connect('proxmox')
pve.create('lxc', {"ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz"})
pve.start('lxc', pve.last_id)
pve.disconnect()
```

## Reference

### Properties

* **hostname** Hostname of the connected node.
* **last_config** Config of the virtual machine represented by `pve.last_id`.
* **last_id** Vmid used in the last run. Only set by methods requiring a vmid.
* **last_technology** Technology used in the last run. Only set by methods requiring a technology.
* **next_id** Next free vmid of the cluster.
* **ssh** Paramiko ssh client.
* **verbose** Verbose output switch.

### Methods

* **add_to_pool(pool_id, pve_vmid_list)** Adds virtual machines to a pool.
* **connect(fqdn, port=22, username='root', password=None, key_filename=None, allow_agent=False)** Connects to a node. If a ssh key is set up on the target node username and password can be omitted. Default paramiko uses the `~/.ssh/id_rsa` key. If you need to use another key use the `key_filename` parameter with the path to the private key file.
* **create(technology, profile, vmid=libpve.last_id, node=libpve.hostname)** Creates a new virtual machine. Possible Values for technology are lxc, openvz and qemu. Can take a profile as dict with virtual machine parameters.
* **create_template(technology, vmid, node=libpve.hostname)** Creates a new template.
* **destroy(technology, vmid, node=libpve.hostname)** Destroys a virtual machine.
* **disconnect(return_status=0)** Disconnects from a node. If a libpve.run throws an exception this method is called automatically to clean up the connection.
* **remove_from_pool(pool_id, pve_vmid_list)** Removes virtual machine from pool.
* **run(cmd)** Runs a command on the node.
* **start(technology, vmid, node=libpve.hostname)** Starts a container.
* **stop(technology, vmid, node=libpve.hostname)** Stops a container.

## Commands

All methods rely on libpve.run to communicate with the target host. It's possible to build an own command for proxmox which is not yet integrated into this library like in the libpve.create method:

```python
def create(self, technology, profile={}, vmid=None, node=None):
        ...
        self.last_id = vmid
        cmd = 'create /nodes/{}/{}'.format(node, technology)
        cmd += ' -vmid {}'.format(vmid)
        for parameter, value in profile.items():
            cmd += ' -{} {}'.format(parameter, value)
        return self.run(cmd)
```

## Verbosity

If you want to enable verbose output initialize the shell like this:

```
pve = libpve.Shell(verbose=True)
```

Verbose output will display the executed command, the return value of the executed command and errors if they are thrown.

## Profiles

An example profile could look like this:

```
{
  "cpulimit": 2,
  "description": "Example container",
  "hostname": "pvecontainer01",
  "memory": 1024,
  "nameserver": "8.8.8.8",
  "net0": "name=eth0,hwaddr=52:4A:5E:26:58:D8,ip=192.168.15.147/24,gw=192.168.15.1,bridge=vmbr0",
  "ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz",
  "password": "changeme",
  "rootfs": 4,
  "storage": "local",
}
```