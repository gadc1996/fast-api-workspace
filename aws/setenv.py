from os import environ
import subprocess
import click
import sys

import _parseenv
import _log as log

AWS_ENV_FILE = environ.get("AWS_ENV_FILE", ".env.aws")


@click.command()
def setenv():
    """Set environment variables in AWS Elastic Beanstalk"""
    env_vars = _parseenv.as_list(AWS_ENV_FILE)
    command = ["eb", "setenv"]
   
    try:
        subprocess.run(command + env_vars, check=True)
    except subprocess.CalledProcessError:
        log.error("Failed to set environment variables in AWS Elastic Beanstalk")
    else:
        log.success("Set environment variables in AWS Elastic Beanstalk")


if __name__ == "__main__":
    setenv()
