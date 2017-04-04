from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.user = 'ubuntu'
env.shell = "/bin/bash -l -i -c"
env.venv = 'microtasking'
env.project_root_folder = 'microtasking'


def pull_latest():
    run("git checkout {}".format(env.branch))
    run("git reset --hard")
    run("git pull")


def collect_staticfiles():
    run('./manage.py collectstatic')


def migrate():
    run('./manage.py migrate')


def install_requirements():
    run('pip install -r requirements.txt')


def restart_uwgsi():
    sudo("systemctl restart uwsgi")


def prod():
    env.hosts = ['ec2-34-252-179-235.eu-west-1.compute.amazonaws.com']
    env.branch = 'master'


def deploy():
    if confirm("You are about to pull and deploy the branch {}. Do you want to continue?".format(env.branch)):
        with cd('/home/ubuntu/{}'.format(env.project_root_folder)), prefix('workon {}'.format(env.venv)):
            pull_latest()
            install_requirements()
            migrate()
            #collect_staticfiles()
            restart_uwgsi()


