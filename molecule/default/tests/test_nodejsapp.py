import os
import pytest
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = ["from-public-git", "from-local-clone"]

def test_nodejs_is_installed(host):
    nodejs = host.package("nodejs").version
    assert nodejs == "16.14.2-deb-1nodesource1"