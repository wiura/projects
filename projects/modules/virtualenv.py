import os

from base import Module
from projects import utils


class Virtualenv(Module):

    required_commands = ['virtualenv', 'pip']
    required_env_vars = ['WORKON_HOME']

    def is_applicable(self, project_data):
        return 'virtualenv' in project_data

    def install(self, project_data):

        dest = os.path.join(os.environ['WORKON_HOME'], project_data['virtualenv']['name'])

        if not utils.dir_exists(dest):
            utils.run('virtualenv %s' % dest)

        with utils.cd(project_data['dir']):
            with utils.workon(project_data['virtualenv']['name']):
                for file in project_data['virtualenv']['files']:
                    utils.run('pip install -r %s' % file)
