import sys

from projects import utils


class Module(object):

    def is_applicable(self, project_data):
        raise NotImplementedError

    required_commands = []

    def check_requirements(self):
        for cmd in self.required_commands:
            if not utils.cmd_exists(cmd):
                utils.error('Command %s is not installed!')
                sys.exit(0)

    def install(self, project_data):
        raise NotImplementedError
