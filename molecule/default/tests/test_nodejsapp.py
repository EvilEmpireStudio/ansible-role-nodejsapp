import os
import pytest
import testinfra.utils.ansible_runner

def test_nodejs_is_installed(host):
    nodejs = host.package("nodejs").version
    assert nodejs == "16.14.2-deb-1nodesource1"