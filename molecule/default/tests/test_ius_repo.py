"""IUS repo testinfra tests."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ius_repo_installed(host):
    """Test package is installed."""
    ius_repo = host.package('ius-release')

    assert ius_repo.is_installed
    # assert ius_repo.version.startswith("")
