#!/usr/bin/env python3

import libpve
import paramiko
import pytest

profile = {
    "description": "Better descriptions",
    "memory": "1024",
    "ostemplate": "local:vztmpl/ubuntu-14.04-standard_14.04-1_amd64.tar.gz",
    "rootfs": "4",
    "storage": "local"
}


class TestShell:

    def test_initialization(self):
        pve = libpve.Shell()
        assert pve.hostname is None
        assert pve.last_id is None
        assert pve.last_technology is None
        assert isinstance(pve.ssh, paramiko.client.SSHClient)
        assert pve.verbose is False

    def test_connection(self):
        pve = libpve.Shell()
        pve.connect('proxmox')
        assert pve.hostname == 'proxmox'
        assert pve.next_id >= 100

    def test_lxc_handling(self):
        pve = libpve.Shell()
        pve.connect('proxmox')
        pve.create('lxc', profile=profile)
        assert isinstance(pve.last_config, dict)
        pve.start('lxc', pve.last_id)
        pve.stop('lxc', pve.last_id)
        pve.destroy('lxc', pve.last_id)
        with pytest.raises(SystemExit) as cm:
            pve.disconnect()
        assert cm.value.code == 0
