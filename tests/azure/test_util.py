import os
import sys

from runway.application_version import ApplicationVersion
from runway.azure import util as victim
from runway.deploy import add_runway_plugin_paths

ENV = ApplicationVersion("dev", "local", "master")


def test_get_default_resource_group():
    res = victim.get_resource_group_name({'azure': {'resource_group_naming': 'rg{env}'}}, ENV)
    assert res == "rgdev"


def test_get_custom_resource_group():
    paths = [os.path.dirname(os.path.realpath(__file__))]
    add_runway_plugin_paths(paths)

    res = victim.get_resource_group_name({}, ENV)
    assert res == "Dave"
    sys.path.remove(paths[0])


def test_get_default_keyvault():
    res = victim.get_keyvault_name({'azure': {'keyvault_naming': 'keyvault{env}'}}, ENV)
    assert res == "keyvaultdev"


def test_get_custom_keyvault():
    paths = [os.path.dirname(os.path.realpath(__file__))]
    add_runway_plugin_paths(paths)

    res = victim.get_keyvault_name({}, ENV)
    assert res == "Mustaine"
    sys.path.remove(paths[0])


def test_get_default_cosmos():
    res = victim.get_cosmos_name({'azure': {'cosmos_naming': 'cosmos{env}'}}, ENV)
    assert res == "cosmosdev"


def test_get_custom_cosmos():
    paths = [os.path.dirname(os.path.realpath(__file__))]
    add_runway_plugin_paths(paths)

    res = victim.get_cosmos_name({}, ENV)
    assert res == "my"
    sys.path.remove(paths[0])


def test_get_default_eventhub():
    res = victim.get_eventhub_name({'azure': {'eventhub_naming': 'eventhub{env}'}}, ENV)
    assert res == "eventhubdev"


def test_get_custom_eventhub():
    paths = [os.path.dirname(os.path.realpath(__file__))]
    add_runway_plugin_paths(paths)

    res = victim.get_eventhub_name({}, ENV)
    assert res == "little"
    sys.path.remove(paths[0])


def test_get_default_kubernetes():
    res = victim.get_kubernetes_name({'azure': {'kubernetes_naming': 'kubernetes{env}'}}, ENV)
    assert res == "kubernetesdev"


def test_get_custom_kubernetes():
    paths = [os.path.dirname(os.path.realpath(__file__))]
    add_runway_plugin_paths(paths)

    res = victim.get_kubernetes_name({}, ENV)
    assert res == "pony"
    sys.path.remove(paths[0])