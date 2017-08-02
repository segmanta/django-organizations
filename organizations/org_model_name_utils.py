from organizations.app_settings import ORGS_ORGANIZATION_MODEL_NAME

def get_org_model_name():
    return ORGS_ORGANIZATION_MODEL_NAME

def format_args(**kwargs):
    return { key.replace('organization', get_org_model_name()): value for key, value in kwargs.iteritems() }

def get_org_field(obj, field_name):
    return getattr(obj, field_name.replace('organization', get_org_model_name()))