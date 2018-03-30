Ansible ius-repo Role
=====================

[![Build Status](https://travis-ci.org/rmachuca89/ansible-ius-repo.svg?branch=master)](https://travis-ci.org/rmachuca89/ansible-ius-repo)

A simple ansible role to install the [IUS repo](https://ius.io/) on RHEL/CentOS based machines.

Requirements
------------

A RHEL/CentOS based OS target host.

Role Variables
--------------

None.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: centos
  roles:
      - ius-repo
```

License
-------

Apache 2.0

Author Information
------------------

Rodrigo Machuca
