from fabric.api import (
    env,
    task,
    run,
    cd,
    hosts,
)

env.use_ssh_config = True

PROD_ENV = 'your server ip'
PROD_USER = 'deploy'

env.user = PROD_USER


@task
@hosts(PROD_ENV)
def deploy():
    with cd('/data/deploy_app/djblog'):
        run('git checkout -- .')
        run('git pull --rebase')
        run('pipenv run python manage.py migrate')
        run('pipenv run python manage.py collectstatic --noinput')
        run('supervisorctl restart djblog')
