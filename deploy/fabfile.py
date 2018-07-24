import random

from fabric import task
from patchwork import files

REPO_URL = 'https://github.com/DerGut/tdd-book.git'


@task
def deploy(c, name):
    print(f'deploying to {name}...')
    site_dir = f"/home/{c.user}/sites/{name}"
    c.run(f"mkdir -p {site_dir}")
    current_commit = c.local('git log -n 1 --format=%H').stdout

    with c.cd(site_dir):
        _get_latest_source(c, current_commit)
        _update_virtualenv(c)
        _create_or_update_dotenv(c, name)
        _update_static_files(c)
        _update_databse(c)


def _get_latest_source(conn, current_commit):
    # Get latest source from github
    if files.exists(conn, '.git'):
        print('fetching from github')
        conn.run('git fetch')
    else:
        print('cloning from github')
        conn.run(f'git clone {REPO_URL} .')

    # Go to the commit of the local machine
    conn.run(f'git reset --hard {current_commit}')


def _update_virtualenv(conn):
    if not files.exists(conn, 'venv/bin/pip'):
        print('creating virtualenv')
        conn.run(f'python3.6 -m venv venv')

    print('installing requirements')
    conn.run('venv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv(conn, name):
    print('updating dotenv')
    files.append(conn, '.env', 'DJANGO_DEBUG_FALSE=y')
    files.append(conn, '.env', f'HOST={conn.host}')
    files.append(conn, '.env', f'SITE_NAME={name}')
    current_contents = conn.run('cat .env').stdout
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        files.append(conn, '.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files(conn):
    print('running collectstatic')
    conn.run('venv/bin/python manage.py collectstatic --noinput')


def _update_databse(conn):
    print('running migrate')
    conn.run('venv/bin/python manage.py migrate --noinput')
