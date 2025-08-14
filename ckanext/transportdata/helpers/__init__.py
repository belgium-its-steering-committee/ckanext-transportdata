import ckan.plugins.toolkit as toolkit
from ckan.logic import NotAuthorized
import re
from ckan.lib.helpers import get_site_protocol_and_host, lang



def scheming_parse_embedded_links(string_with_links):
    """
    Parse string text that contains links. Links should be added as `<a href="/your/link">link text</a>`.
    If the link start with `/`, it is considered as a relative link
    and will automatically get prefixed with the correct language code. (e.g. `/pages/your-page` becomes `/en/pages/your-page`)
    if not, the link is kept as is.
    :param string_with_links: input string containing <a href="...">link text</a>
    :return: list of parts with text and href information. If no links, will contain one (normal-text) part
    """
    parts_list = []
    
    # match <a href='...'>link text</a>
    pattern = r'<a\s+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>'
    
    last_link_match_end = 0
    for match in re.finditer(pattern, string_with_links):
        # text starting from end last link (or beginning) till before this link
        parts_list.append({
            "text": string_with_links[last_link_match_end:match.start()],
            "href": None
        })
        
        # link itself
        href = match.group(1)
        link_text = match.group(2)

        if href.startswith('/'):
            protocol, host = get_site_protocol_and_host()
            if protocol and host:
                href = f"{protocol}://{host}/{lang()}{href}"
        
        parts_list.append({ "text": link_text,"href": href })
        
        last_link_match_end = match.end()
    
    # text after last link
    if last_link_match_end < len(string_with_links):
        parts_list.append({ "text": string_with_links[last_link_match_end:], "href": None })
    
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