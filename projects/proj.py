import yaml
import commands


def run():
    with open('projects') as f:
        data = f.read()

    data = yaml.load(data)

    for project_data in data:
        commands.install(project_data)
