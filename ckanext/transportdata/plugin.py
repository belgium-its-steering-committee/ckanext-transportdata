import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
# import ckanext.transportdata.cli as cli
# import ckanext.transportdata.views as views

from ckanext.transportdata.uploader import OrganizationUploader


@plugins.toolkit.blanket.auth_functions
@plugins.toolkit.blanket.actions
@plugins.toolkit.blanket.helpers
@plugins.toolkit.blanket.validators
class TransportdataPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IUploader)
    
    # IUploader
    
    def get_uploader(self, upload_to, old_filename):
        if upload_to == "group":
            return OrganizationUploader(upload_to, old_filename)
        return None

    def get_resource_uploader(self, data_dict):
        return None

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "transportdata")

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()
