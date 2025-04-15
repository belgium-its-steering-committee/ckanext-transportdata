"""Tests for helpers.py."""

import ckanext.transportdata.helpers as helpers


def test_transportdata_hello():
    assert helpers.transportdata_hello() == "Hello, transportdata!"
