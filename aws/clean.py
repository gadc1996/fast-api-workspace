import click
import subprocess

import _log as log


@click.command()
def clean():
    """Clean up AWS Elastic Beanstalk application and environment"""
    command = ["eb", "terminate", "--all", "--force"]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        log.error(
            "Failed to clean up AWS Elastic Beanstalk application and environment"
        )
    else:
        log.success("Cleaned up AWS Elastic Beanstalk application and environment")


if __name__ == "__main__":
    clean()
