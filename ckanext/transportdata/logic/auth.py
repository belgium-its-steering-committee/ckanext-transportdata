import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def transportdata_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "transportdata_get_sum": transportdata_get_sum,
    }
