from flask import current_app

ENV = 'prod'


def is_web():
    is_web = False
    try:
        if hasattr(current_app, 'run_env'):
            is_web = True
    except:
        pass
    return is_web


def get_env():
    env = ENV
    if is_web():
        env = current_app.run_env
    return env

