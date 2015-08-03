Projects
========

Example projects file:
```
- name: my_project
  dir: ~/Code/my_project
  git:
    repo: git@bitbucket.org:user/my_project.git
  npm:
    dir: .
  bower:
    dir: .
  virtualenv:
    name: my_project
    files:
      - my_project/requirements.txt

```
