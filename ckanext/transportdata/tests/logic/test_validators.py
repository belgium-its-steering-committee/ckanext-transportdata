"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.transportdata.logic import validators


def test_transportdata_reauired_with_valid_value():
    assert validators.transportdata_required("value") == "value"


def test_transportdata_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.transportdata_required(None)
