import ckan.plugins.toolkit as tk

from logging import getLogger
log = getLogger(__name__)

@tk.auth_allow_anonymous_access
def transportdata_get_sum(context, data_dict):
    return {"success": True}


def member_list(context, data_dict):
    return {"success": False}
