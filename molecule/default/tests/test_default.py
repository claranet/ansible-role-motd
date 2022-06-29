#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

motd_file_path = "/usr/local/bin/dynmotd"
pam_line = f"session optional pam_exec.so type=open_session stdout {motd_file_path}"


def test_motd_file(host):
    file = host.file(motd_file_path)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o755


def test_motd_output(host):
    command = host.run(motd_file_path)
    assert command.succeeded
    assert command.stderr == ""
    print(f"\n{command.stdout}")


def test_pam_login_file(host):
    file = host.file("/etc/pam.d/login")
    assert file.exists
    assert file.contains(pam_line)


def test_pam_sshd_file(host):
    file = host.file("/etc/pam.d/sshd")
    assert file.exists
    assert file.contains(pam_line)
