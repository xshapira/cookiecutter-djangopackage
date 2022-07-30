import re
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('pre_gen_project')

APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

app_name = '{{cookiecutter.app_name}}'

if not re.match(APP_REGEX, app_name):
    logger.error(f'Invalid value for app_name "{app_name}"')
    sys.exit(1)

ALLOWED_VERSIONS = ["1.11", "2.1", "master"]

for django_version in '{{cookiecutter.django_versions}}'.split(","):
    if str(django_version).strip() not in ALLOWED_VERSIONS:
        logger.error(f'Invalid Django version "{django_version}". ')
        sys.exit(1)
