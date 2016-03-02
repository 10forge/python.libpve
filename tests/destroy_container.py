#!/usr/bin/env python

import libpve
import sys

vmid = sys.argv[1]
if vmid == '':
    print('vmid missing')
    sys.exit(1)

pve = libpve.Shell()
pve.connect('proxmox')
pve.stop('lxc', vmid)
pve.destroy('lxc', vmid)
