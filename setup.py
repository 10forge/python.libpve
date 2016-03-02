from setuptools import setup, find_packages

setup(
    author='Thomas Steinert',
    author_email='monk@10forge.org',
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration'
    ],
    description='Python interface for interacting with proxmox.',
    install_requires=[
        'paramiko>=1.16.0'
    ],
    keywords=['api', 'http', 'proxmox', 'pve', 'shell'],
    license='not ready for distribution',
    name='libpve',
    packages=find_packages('libpve'),
    url='https://github.com/m-o-n-k/libpve.git',
    version='0.1.0',
    zip_safe=False)
