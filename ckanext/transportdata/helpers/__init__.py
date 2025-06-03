import ckan.plugins.toolkit as toolkit
from ckan.logic import NotAuthorized

# Copied from https://github.com/belgium-its-steering-committee/ckanext-scheming/blob/MobilityDCAT/root/ckanext/scheming/helpers.py#L348
def scheming_split_help_text_by_link(help_text):
    """
    Split help text in different parts by looking for '<a>' tags
    :param help_text: input help text
    :return: list of parts
    """
    parts_list = []
    if "<a>" in help_text:
        parts = help_text.split("<a>")
        parts2 = parts[1].split("</a>")
        parts_list.append({"text": parts[0], "link": False})
        parts_list.append({"text": parts2[0], "link": True})
        parts_list.append({"text": parts2[1], "link": False})
    else:
        parts_list.append({"text": help_text, "link": False})
    return parts_list


def transportdata_is_member_of_org(org_id, user_id):
    if not user_id:
        return False
    try:
        members = toolkit.get_action('member_list')({}, {
            'id': org_id
        })

        return any(
            member_type == 'user' and member_id == user_id 
            for member_id, member_type, _ in members
        )
    except NotAuthorized:
        return False