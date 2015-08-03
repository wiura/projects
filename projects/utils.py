from contextlib import contextmanager
import os
import subprocess
import threading

local = threading.local()


def info(str):
    print '\x1b[1;32mINFO: %s \x1b[0m' % str


def default(str):
    print str


def warning(str):
    print '\x1b[1;33mWARNING: %s \x1b[0m' % str


def error(str):
    print '\x1b[0;31mERROR: %s \x1b[0m' % str


def dir_exists(dir):
    return os.path.isdir(dir)


def get_project_dir(project_abs_dir, project_dir_abs_or_rel):
    if project_dir_abs_or_rel.startswith('/') or project_dir_abs_or_rel.startswith('~'):
        return project_dir_abs_or_rel.replace('~', os.path.expanduser('~'))
    return os.path.join(project_abs_dir, project_dir_abs_or_rel)


def set_current_dir(dir):
    local.curdir = dir


def get_current_dir():
    curdir = getattr(local, 'curdir', None)
    if not curdir:
        return os.getcwd()
    return curdir


def set_current_virtualenv(virtualenv):
    local.curvirtualenv = virtualenv


def get_current_virtualenv():
    return getattr(local, 'curvirtualenv', None)


def cmd_exists(cmd):
    return subprocess.call(
        'type ' + cmd,
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ) == 0

@contextmanager
def cd(dir_abs_or_rel):
    olddir = get_current_dir()

    if dir_abs_or_rel.startswith('/') or dir_abs_or_rel.startswith('~'):
        set_current_dir(dir_abs_or_rel.replace('~', os.path.expanduser('~')))
    else:
        newdir = os.path.join(olddir, dir_abs_or_rel)
        set_current_dir(newdir)

    yield

    set_current_dir(olddir)


def run(command):
    virtualenv = get_current_virtualenv()

    if virtualenv is not None:
        default('(%s) > %s' % (virtualenv.split('/')[-3], command))
    else:
        default('> %s' % command)

    if virtualenv is not None:
        command = 'source %s; %s' % (virtualenv, command)

    subprocess.call(command, cwd=get_current_dir(), shell=True)


@contextmanager
def workon(virtualenv_name):
    dest = os.path.join(os.environ['WORKON_HOME'], virtualenv_name, 'bin', 'activate')

    set_current_virtualenv(dest)

    yield

    set_current_virtualenv(None)
