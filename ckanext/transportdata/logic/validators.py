import ckan.plugins.toolkit as tk


def transportdata_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "transportdata_required": transportdata_required,
        'logo_extensions': logo_validator,
        'doc_validator': pdf_validator,
    }

# Copied from https://github.com/belgium-its-steering-committee/ckanext-scheming/blob/MobilityDCAT/root/ckanext/scheming/validation.py#L324
def logo_validator(value):
    if value and len(value) > 0:
        if not value.endswith(('jpeg', 'JPEG', 'jpg','JPG','bmp','BMP', "PNG", "png")):
            raise Invalid(_('Only supported image formats are allowed: jpeg, jpg, bmp, png'))
    return value

def pdf_validator(value):
    if value and len(value) > 0:
        if not value.endswith(('pdf', 'PDF')):
            raise Invalid(_('Only PDF is allowed').format(url=value))
    return value