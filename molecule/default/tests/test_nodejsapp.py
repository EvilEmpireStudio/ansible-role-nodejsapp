import os
import pytest
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = ["from-public-git", "from-local-clone"]

def test_nodejs_is_installed(host):
    assert host.package("nodejs").is_installed
