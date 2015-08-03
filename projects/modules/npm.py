from base import Module
from projects import utils


class Npm(Module):

    required_commands = ['npm']

    def is_applicable(self, project_data):
        return 'npm' in project_data

    def install(self, project_data):

        npm_dir = utils.get_project_dir(project_data['dir'], project_data['npm']['dir'])

        with utils.cd(npm_dir):
            utils.run('npm install')
