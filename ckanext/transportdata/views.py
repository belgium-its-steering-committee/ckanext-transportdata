from flask import Blueprint


transportdata = Blueprint(
    "transportdata", __name__)


def page():
    return "Hello, transportdata!"


transportdata.add_url_rule(
    "/transportdata/page", view_func=page)


def get_blueprints():
    return [transportdata]
