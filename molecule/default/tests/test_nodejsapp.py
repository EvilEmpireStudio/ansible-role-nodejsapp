import os
import pytest
import requests
import testinfra.utils.ansible_runner

def test_nodejs_is_installed(host):
    nodejs = host.package("nodejs").version
    assert nodejs == "16.14.2-deb-1nodesource1"

def test_application_from_git_main_directory_presence(host):
    assert host.file("/opt/hello-from-git").exists
    assert host.file("/opt/hello-from-git").is_directory

def test_application_from_git_service(host):
    assert host.service("hello-from-git").is_valid
    assert host.service("hello-from-git").is_running
    assert host.service("hello-from-git").is_enabled

def test_application_from_git_socket_listening(host):
    assert host.socket("tcp://3000")

def test_application_from_git_reponse_200(host):
    ip = host.ansible.get_variables()['ansible_host']
    r = requests.get(f"http://{ip}:3000")
    assert r.status_code == 200