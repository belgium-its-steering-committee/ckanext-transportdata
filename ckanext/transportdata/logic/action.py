import ckan.plugins.toolkit as tk
import ckanext.transportdata.logic.schema as schema


@tk.side_effect_free
def transportdata_get_sum(context, data_dict):
    tk.check_access(
        "transportdata_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.transportdata_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'transportdata_get_sum': transportdata_get_sum,
    }
