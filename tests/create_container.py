#!/usr/bin/env python

import libpve

profile = {
    "ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz"
}

pve = libpve.Shell()
pve.connect('proxmox')
pve.create('lxc', profile)
