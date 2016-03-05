# libpve

Python interface for interacting with proxmox.

## Getting started

```python
import libpve

pve = libpve.Shell()
pve.connect('proxmox')
print(pve.create('lxc', {"ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz"))
print(pve.start('lxc', pve.last_id))
```

## Reference

### Properties

* **hostname** Hostname of the connected node.
* **last_id** Vmid used in the last run. Not every method sets libpve.last_id. See the methods section for more infos.
* **next_id** Next free vmid of the cluster.
* **ssh** Paramiko ssh client.

### Methods

* **add_to_pool(pool_id, pve_vmid_list)** Adds virtual machines to a pool.
* **create(technology, profile={}, vmid=libpve.last_id, node=libpve.hostname)** Creates a new virtual machine. Possible Values for **technology** are `lxc`, `openvz` and `qemu`. Can take a profile as dict with virtual machine parameters. Sets libpve.last_id.
* **create_template(technology, vmid, node=libpve.hostname)** Creates a new template. Sets libpve.last_id.
* **remove_from_pool(pool_id, pve_vmid_list)** Removes virtual machine from pool.
* **destroy(technology, vmid, node=libpve.hostname)** Destroys a virtual machine. Sets libpve.last_id.
* **run(cmd, silent=False)** Runs a command on the node.
* **connect(fqdn, port=22, username='root', password=None)** Connects to a node. If a ssh key is set up on the target node username and password can be omitted.
* **disconnect()** Disconnects from a node. If a libpve.run throws an exception this method is called automatically to clean up the connection.
* **start(technology, vmid, node=libpve.hostname)** Starts a container. Sets libpve.last_id.
* **stop(technology, vmid, node=libpve.hostname)** Stops a container. Sets libpve.last_id.

## Commands

All methods rely on libpve.run to communicate with the target host. It's possible to build an own command for proxmox which is not yet integrated into this library like in the libpve.create method:

```python
def create(self, technology, profile={}, vmid=None, node=None):
        ...
        self.last_id = vmid
        cmd = 'create /nodes/{}/{}'.format(node, technology)
        cmd += ' -ostemplate {}'.format(ostemplate)
        cmd += ' -vmid {}'.format(vmid)
        return self.run(cmd)
```
