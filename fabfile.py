from fabric.api import (
    env,
    task,
    run,
    cd,
)

env.use_ssh_config = True

PROD_ENV = 'your server ip'
PROD_USER = 'deploy'

env.user = PROD_USER


@task
def deploy_web():
    with cd('/data/deploy_app/djblog'):
        run('git checkout -- .')
        run('git pull --rebase')
        run('python manage.py migrate')
        run('python manage.py collectstatic')
        run('supervisor restart djblog')
