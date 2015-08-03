from base import Module
from projects import utils


class Git(Module):

    required_commands = ['git']

    def is_applicable(self, project_data):
        return 'git' in project_data

    def install(self, project_data):

        if utils.dir_exists(project_data['dir']):
            return

        git = project_data['git']

        utils.run('git clone %s %s' % (git['repo'], project_data['dir']))
