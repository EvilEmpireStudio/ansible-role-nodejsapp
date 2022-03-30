import os
import pytest
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = ["from-local-clone"]

def test_application_from_local_clone_main_directory_presence(host):
    assert host.file("/opt/hello-from-local-clone").exists
    assert host.file("/opt/hello-from-local-clone").is_directory

def test_application_from_local_clone_service(host):
    assert host.service("hello-from-local-clone").is_valid
    assert host.service("hello-from-local-clone").is_running
    assert host.service("hello-from-local-clone").is_enabled

def test_application_from_local_clone_socket_listening(host):
    assert host.socket("tcp://8081")

def test_application_from_local_clone_reponse_200(host):
    ip = host.ansible.get_variables()['ansible_host']
    print(ip)
    r = requests.get(f"http://{ip}:8081")
    assert r.status_code == 200