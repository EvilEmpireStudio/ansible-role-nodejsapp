import os
import pytest
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = ["from-public-git"]

def test_application_from_git_main_directory_presence(host):
    assert host.file("/opt/hello-from-git").exists
    assert host.file("/opt/hello-from-git").is_directory

def test_application_from_git_service(host):
    assert host.service("hello-from-git").is_valid
    assert host.service("hello-from-git").is_running
    assert host.service("hello-from-git").is_enabled

def test_application_from_git_socket_listening(host):
    assert host.socket("tcp://8080")

def test_application_from_git_reponse_200(host):
    ip = host.ansible.get_variables()['ansible_host']
    print(ip)
    r = requests.get(f"http://{ip}:8080")
    assert r.status_code == 200
