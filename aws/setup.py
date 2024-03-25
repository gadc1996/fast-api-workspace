import subprocess
import os
import sys
import secrets
import click

import _parseenv
import _log as log

AWS_REGION = os.environ.get("AWS_REGION")
AWS_PLATFORM = os.environ.get("AWS_PLATFORM")
AWS_ENV_FILE = os.environ.get("AWS_ENV_FILE")
APP_NAME = os.environ.get("APP_NAME")


@click.command()
def setup() -> None:
    """Setup AWS Elastic Beanstalk application and environment with database"""
    _validate_env_vars()
    _setup_app()
    _setup_enviroment()


def _validate_env_vars() -> None:
    env_vars = ["AWS_REGION", "AWS_PLATFORM", "APP_NAME", "AWS_ENV_FILE"]

    for var in env_vars:
        if not globals().get(var):
            log.error(f"Please set {var} environment variable.")
            sys.exit(1)
    
    log.success("Validated environment variables")
            
    


def _setup_app() -> None:
    try:
        subprocess.run(
            ["eb", "init", "--platform", AWS_PLATFORM, "--region", AWS_REGION, APP_NAME],
            check=True,
        )
    except subprocess.CalledProcessError:
        log.error("Failed to setup AWS Elastic Beanstalk application")
    else:
        log.success("Setup AWS Elastic Beanstalk application")


def _setup_enviroment() -> None:
    env_vars = _parseenv.as_string(AWS_ENV_FILE)
    command = [
        "eb",
        "create",
        f"{APP_NAME}-dev",
        "--single",
        "--cname",
        f"{APP_NAME}-dev",
        "--envvars",
        env_vars,
        "--database",
        "--database.engine",
        "mysql",
        "--database.username",
        "ebroot",
        "--database.password",
        secrets.token_urlsafe(16),
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        log.error("Failed to setup AWS Elastic Beanstalk environment")
    else:
        log.success("Setup AWS Elastic Beanstalk environment")


if __name__ == "__main__":
    setup()
