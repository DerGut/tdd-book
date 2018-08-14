from fabric import Connection


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)

    conn = Connection(host=host, user='jsteinmann')
    conn.run(f'{manage_dot_py} flush --noinput')


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    conn = Connection(host=host, user='jsteinmann')
    env_vars = _get_server_env_vars(conn)

    session_key = conn.run(f'{manage_dot_py} create_session {email}', env=env_vars)

    return session_key.strip()


def _get_manage_dot_py(host):
    return f'~/sites/{host}/venv/bin/python ~/sites/{host}/manage.py'


def _get_server_env_vars(conn):
    env_lines = conn.run(f'cat ~/sites/{conn.host}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)
