from modules import modules_dict
import utils


def install(project_data):

    utils.info('Installing %s...' % project_data['name'])

    for cls in modules_dict:
        if cls.is_applicable(project_data):
            cls.check_requirements()

    for cls in modules_dict:
        if cls.is_applicable(project_data):
            cls.install(project_data)

    utils.info('Finished installing %s' % project_data['name'])
