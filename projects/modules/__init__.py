from git import Git
from npm import Npm
from bower import Bower
from virtualenv import Virtualenv

modules_dict = [
    Git(),
    Npm(),
    Bower(),
    Virtualenv()
]
