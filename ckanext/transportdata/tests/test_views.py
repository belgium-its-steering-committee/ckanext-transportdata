"""Tests for views.py."""

import pytest

import ckanext.transportdata.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "transportdata")
@pytest.mark.usefixtures("with_plugins")
def test_transportdata_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("transportdata.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, transportdata!"
