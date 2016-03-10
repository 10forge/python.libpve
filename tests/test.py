#!/usr/bin/env python3

import libpve

profile={
    "description": "Better descriptions",
    "memory": "1024",
    "ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz",
    "rootfs": "4",
    "storage": "local"
}

pve = libpve.Shell(verbose=True)
pve.connect('proxmox')
pve.create('lxc', profile=profile)
pve.add_to_pool('pool2', pve.last_id)
pve.start('lxc', pve.last_id)
pve.stop('lxc', pve.last_id)
pve.destroy('lxc', pve.last_id)
