# Ansible role - motd
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-motd?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-motd?style=flat-square)](https://github.com/claranet/ansible-role-motd/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-motd/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-motd/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.9-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/motd)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure dynamic MOTD

This role uses [https://github.com/claranet/motd](https://github.com/claranet/motd) by default to get the MOTD

```
System info:
  Hostname·········: claranet_motd_ubuntu-20.04
  Distro···········: Ubuntu 20.04.3 LTS
  Kernel···········: Linux 5.10.47-linuxkit
  Uptime···········: up 2 days, 23 hours, 18 minutes
  Load·············: 1.33 (1m), 0.43 (5m), 0.20 (15m)
  Processes········: 13 (root), 3 (user), 16 (total)
  CPU··············: Intel(R) Core(TM) i7-8569U CPU @ 2.80GHz (4 vCPU)
  Memory···········: 626Mi used, 2.6Gi avail, 3.8Gi total
  Local IPs········: 172.17.0.6

Disk usage:
  /                               9% used out of  63G
  [====··············································]

Ansible:
  Last deployment···: 2021-09-27T13:33:33.665714Z
```

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.motd
```

## :gear: Role variables

Variable                     | Default value                                                          | Description
-----------------------------|------------------------------------------------------------------------|----------------------------------------------------------------
motd_disable_default_motd    | true                                                                   | Disable system default MOTD (/etc/motd)
motd_template                | https://raw.githubusercontent.com/claranet/motd/master/scripts/00-basic| Dynmaic MOTD template<br>Can be a URL or a local template
motd_template_prepend        | ""                                                                     | Prepend raw content to `motd_template`
motd_template_append         | See [defaults/main.yml](defaults/main.yml)                             | Append raw content to `motd_template`
motd_template_username       | ""                                                                     | Used when `motd_template` is an URL
motd_template_password       | ""                                                                     | Used when `motd_template` is an URL

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - role: claranet.motd
      motd_template: "{{ playbook_dir }}/templates/dynmotd.j2"
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
