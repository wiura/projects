from base import Module
from projects import utils


class Bower(Module):

    required_commands = ['bower']

    def is_applicable(self, project_data):
        return 'bower' in project_data

    def install(self, project_data):

        bower_dir = utils.get_project_dir(project_data['dir'], project_data['bower']['dir'])

        with utils.cd(bower_dir):
            utils.run('bower install')
